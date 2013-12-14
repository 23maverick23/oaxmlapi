# oaxmlapi

## DESCRIPTION
oaxmlapi is a Python wrapper around the NetSuite OpenAir XML API.

This library allows for easier interaction with the XML API, and reduces the need to generate raw XML. The library is written entirely in Python and utilizes the etree.ElementTree library for producing pre-formatted XML tags and attributes for use in your API requests.

## AUTHORS
Ryan Morrissey - [ryancmorrissey.com](http://ryancmorrissey.com)

## LICENSE
See [LICENSE.md](LICENSE.md)

## REQUIREMENTS
- Python 2.5+ (2.7.3 recommended)
- pytest 2.3.5+

## INSTALLATION
For Windows, download the latest build [here](https://github.com/23maverick23/oaxmlapi/archive/master.zip) as archive. Unpack the archive and run `python setup.py install` inside the root directory.

For Linux and Mac OSX, you can use Terminal/iTerm to download, unpack and install.
```bash
$ curl -LOk https://github.com/23maverick23/oaxmlapi/archive/master.zip
$ unzip master.zip
$ cd oaxmlapi-master
$ sudo python setup.py install
```

## DOCUMENTATION
Documentation for this package can be found on the [oaxmlapi wiki](https://github.com/23maverick23/oaxmlapi/wiki).

Documentation for the NetSuite OpenAir XML API can be found in the [PDF guide](http://www.openair.com/download/OpenAirXMLAPIGuide.pdf).

## BUGS
Please use [issues](https://github.com/23maverick23/oaxmlapi/issues) for logging and tracking bugs or enhancements.

## CREDITS
See [CREDITS](CREDITS)

## HISTORY
Current Version: 1.1

* Small bug fixes

Version 1.0

* Initial commit
