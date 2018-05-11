# Basic Usage

## Simple Example

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

{% hint style="danger" %}
This package is not designed to do any validation or type checking on your API inputs - it is simply a wrapper around the OpenAir XML API allowing you to write more Pythonic objects which easily convert to XML bytestrings for use in HTTP requests.
{% endhint %}



