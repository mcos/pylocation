"""
Main PyLocate Module
"""

import requests

try:
    # python 2.6 and greater
    import json
except ImportError:
    try:
        # python 2.5
        import simplejson
        json = simplejson
    except ImportError:
        # if we're in django or Google AppEngine land
        # use this as a last resort
        from django.utils import simplejson
        json = simplejson

"""
All the constants we need
"""
BASE_URL = "http://api.hostip.info/%s"
HTML_URL = BASE_URL % "get_html.php?ip="
XML_URL = BASE_URL % "ip="
JSON_URL = BASE_URL % "get_json.php?ip="

class PylocateError(Exception):
    pass

class PylocateResponseError(Exception):
    def __init__(self):
        pass

class HTTPBackend(object):
    pass

class Pylocate(object):
    def __init__(self,ipaddress=None):
        pass