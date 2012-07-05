PyLocation
========

A Python Module to wrap the IP address geolocation service from [hostip.info](http://www.hostip.info).


## Installation
Download the tarball, untar and run `python setup.py install`

## Dependencies
`pylocation` depends on the excellent [requests](https://github.com/kennethreitz/requests) library.

## Usage

    from pylocation import PyLocation

    # Initializing without specifying an IP Address gives us the IP information
    # from the machine using this module
    pyloc = PyLocation()

    # Same as above, but includes the GPS Coordinates
    pyloc = PyLocation(position=True)

    # Initializing with an IP address
    pyloc = PyLocation(ip='8.8.8.8')

    # Same as above, but includes the GPS Coordinates
    pyloc = PyLocation(ip='8.8.8.8', position=True)

    # Outputs
    pyloc.text # Returns the information as a unicode string
    pyloc.jsontext # Returns the information as a JSON string
    pyloc.json # Returns the information as JSON parsed to a dictionary
    pyloc.xmltext # Returns the information as an xml string
    pyloc.xml # Returns the information as an XML Element Tree
    """
    The following returns the information as a python object
    """
    pylocinfo = pyloc.info
    pylocinfo.ip => '8.8.8.8'
    pylocinfo.city => 'Mountain View, CA'
    pylocinfo.country_name => 'UNITED STATES'
    pylocinfo.country_code => 'US'
    pylocinfo.latitude => '37.402'
    pylocinfo.longitude => '-122.078'


    """
    If you're getting the info for multiple IP addresses, you don't need to
    create multiple PyLocation objects
    """

    pyloc = PyLocation()
    pyloc.json # Returns the JSON representation of the geolocation info for the IP of the host machine
    pyloc.ip = '8.8.8.8' # Change the IP to 8.8.8.8
    pyloc.position = True # Include the GPS Coordinates
    pyloc.json # Returns the JSON representation of geolocation info for IP 8.8.8.8

## Contributors
 * [Mark Costello](http://github.com/mcos)
