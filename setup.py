from distutils.core import setup

setup(name = 'pylocation',
      version = '0.2',
      description = 'Python Wrapper Library for Geolocating IP Addresses',
      author = 'Mark Costello',
      author_email = 'me@markcostello.net',
      url = 'https://github.com/mcos/pylocation',
      license = "MIT License",
      install_requires = ['requests'],
      packages = ['pylocation']
     )