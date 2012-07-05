from distutils.core import setup

setup(name = 'pylocation',
      version = '0.1',
      description = 'Python Wrapper Library for Geolocating IP Addresses',
      author = 'Mark Costello',
      author_email = 'me@markcostello.net',
      url = 'https://github.com/mcos/pylocate',
      license = "MIT License",
      install_requires = ['requests'],
      packages = ['pylocation']
     )