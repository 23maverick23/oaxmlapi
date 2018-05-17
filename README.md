# oaxmlapi

![PyPI](https://img.shields.io/pypi/23maverick23/oaxmlapi.svg) ![Codecov](https://img.shields.io/codecov/c/github/23maverick23/oaxmlapi.svg) ![Travis](https://img.shields.io/travis/23maverick23/oaxmlapi.svg) ![license](https://img.shields.io/github/license/23maverick23/oaxmlapi.svg) ![GitHub top language](https://img.shields.io/github/languages/top/23maverick23/oaxmlapi.svg) ![OpenAir release](https://img.shields.io/badge/OpenAir%20Release-2018.1-green.svg)

## DESCRIPTION
oaxmlapi is a Python wrapper around the NetSuite OpenAir XML API. It allows for easier interaction with the XML version of the OpenAir API and reduces the need to generate raw XML. The library is written entirely in Python and utilizes the etree.ElementTree library for producing pre-formatted XML tags and attributes for use in your API requests.

## REQUIREMENTS
* Python 2.6, 2.7, 3.5, 3.6
* coverage [view source](https://bitbucket.org/ned/coveragepy)
* codecov [view source](https://github.com/codecov/codecov-python)

## INSTALLATION

### PyPI

Coming soon!

### Manual

For Windows, download the latest build [here](https://github.com/23maverick23/oaxmlapi/archive/master.zip) as archive. Unpack the archive and run `python setup.py install` inside the root directory.

For Linux and Mac OSX, you can use Terminal/iTerm to download, unpack and install.
```bash
$ curl -LOk https://github.com/23maverick23/oaxmlapi/archive/master.zip
$ unzip master.zip
$ cd oaxmlapi-master
$ sudo python setup.py install
```

## DOCUMENTATION

- Documentation for this package can be found on Gitbook at [https://23maverick23.gitbook.io/oaxmlapi/](https://23maverick23.gitbook.io/oaxmlapi/).
- Documentation for the NetSuite OpenAir XML API can be found at [http://www.openair.com/download/OpenAirXMLAPIGuide.pdf](http://www.openair.com/download/OpenAirXMLAPIGuide.pdf).

## BASIC EXAMPLE

The focus of this package is simple - write Python, not XML. Here's an example which uses the `urllib2` library to make a simple HTTP request using some XML formatted data.

```python
import urllib2
from oaxmlapi import connections, datatypes, commands

app = connections.Application('test app', '1.0', 'default', 'uniquekey')
auth = connections.Auth('My Company', 'Admin', 'p@ssw0rd')

date = datatypes.Datatype('Date', {'month': '03', 'day': '14', 'year': '2012'})
task = datatypes.Datatype('Task', {'projectid': '13'})

filter1 = commands.Read.Filter('newer-than', 'date', date).getFilter()
filter2 = commands.Read.Filter(None, None, task).getFilter()

xml_data = []
xml_data.append(commands.Read('Task', 'equal to', {'limit': '1000'}, [filter1, filter2], ['id', 'timesheetid']).read())
xml_req = connections.Request(app, auth, xml_data).tostring()

req = urllib2.Request(url='https://www.openair.com/api.pl', data=xml_req)
```

## AUTHORS
Ryan Morrissey - [ryancmorrissey.com](https://ryancmorrissey.com/)
