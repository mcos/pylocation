"""
Main PyLocation Module
"""

import requests
from xml.etree import ElementTree as ET

BASE_URL = "http://api.hostip.info/%s"
XML_URL = BASE_URL % ""
HTML_URL = BASE_URL % "get_html.php"
JSON_URL = BASE_URL % "get_json.php"

class PyLocationError(Exception):
    """A generic PyLocation Exception"""

    def __init__(self):
        super(PyLocationError, self).__init__()

class PyLocationResponseError(PyLocationError):
    """A PyLocation Exception for any invalid response from the GeoLocation
    service.
    """

    def __init__(self, response):
        super(PyLocationResponseError, self).__init__()
        self.status_code = response.status_code
        self.content = response.content

class HTTPBackend(object):
    """The :class `HTTPBackend` object. Carries out all the HTTP Operations for
    PyLocation.
    """

    def __init__(self):
        self.request = requests

    def get(self, url, params=None):
        try:
            response = self.request.get(url, params=params)
            if response.status_code != 200:
                raise PyLocationResponseError(response)
            return response
        except PyLocationError, pylocerr:
            raise pylocerr

class LocationInfo(object):
    """The :class `LocationInfo` object. Used to transform the location info
    dictionary to an object.
    """

    def __init__(self, properties):
        for prop in properties:
            prop_name = prop
            if prop_name == 'lat':
                prop_name = 'latitude'
            elif prop_name == 'lng':
                prop_name = 'longitude'
            setattr(self, prop_name, properties[prop])
    def __init__(self, properties):
        self.ip = properties['ip']
        self.city = properties['city']
        self.country_name = properties['country_name']
        self.country_code = properties['country_code']
        self.latitude = properties.get('lat',None)
        self.longitude = properties.get('lng',None)

class PyLocation(object):
    """The :class `PyLocation` object. Used to perform the various operations
    for getting the location of an IP Address
    """

    def __init__(self, ip=None, position=False):
        self.ip = ip
        self.position = position
        self.httpbackend = HTTPBackend()

    def get_params(self):
        params = {}
        params['ip'] = self.ip
        if self.position:
            params['position'] = self.position
        return params

    @property
    def text(self):
        resp = self.httpbackend.get(HTML_URL, params=self.get_params())
        return resp.text

    @property
    def jsontext(self):
        resp = self.httpbackend.get(JSON_URL, params=self.get_params())
        return resp.text

    @property
    def json(self):
        resp = self.httpbackend.get(JSON_URL, params=self.get_params())
        return resp.json

    @property
    def xmltext(self):
        resp = self.httpbackend.get(XML_URL, params=self.get_params())
        return resp.text

    @property
    def xml(self):
        xmlstr = self.xmltext
        parsedxml = ET.XML(xmlstr)
        return parsedxml

    @property
    def info(self):
        return LocationInfo(self.json)
