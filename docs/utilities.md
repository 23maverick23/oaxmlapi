---
description: The utilities.py module provides a few helper methods for working with XML.
---

# Utilities

### tostring

This utility method can be called on any `_Base` subclass objects and returns a string representation of the _ElementTree_ object.

```python
my_date = datatypes.Datatype(
    'Date',
    {
        'month': '03',
        'day': '14',
        'year': '2012',
        'hour': '08',
        'minute': '35',
        'second': '43'
    }
)
print(my_date.tostring())
>>> b'<Date><hour>08</hour><month>03</month><second>43</second><year>2012</year><day>14</day><minute>35</minute></Date>'
```

### prettify

This utility method can be called on any `_Base` subclass objects and returns a formatted, prettified string representation of the _ElementTree_ object.

```python
my_date = datatypes.Datatype(
    'Date',
    {
        'month': '03',
        'day': '14',
        'year': '2012',
        'hour': '08',
        'minute': '35',
        'second': '43'
    }
)

print(my_date.prettify())
>>> b'''
<?xml version="1.0" encoding="utf-8"?>
<Date>
  <hour>08</hour>
  <month>03</month>
  <second>43</second>
  <year>2012</year>
  <day>14</day>
  <minute>35</minute>
</Date>
'''
```

## xml2json

This utility method converts an XML string into a JSON string, which for some users will be easier to work with than an XML string. An example for this helper method can be found below.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| xmlstring | String | an XML string |
| strip | Bool | string whitespace (default: True) |

{% hint style="info" %}
You can use `simplejson.dumps()` or `json.dumps()` to convert the JSON string into a JSON object. Tag text is accessed using standard `key[value]` syntax, and tag attributes are accessed using `@attrib` syntax. Any tails within a tag are accessed using `#tail` syntax.
{% endhint %}

```python
import urllib2
import json  # or use json module
from oaxmlapi import utilities

res = urllib2.urlopen(req)
xml_res = res.read()
>>> '<response><Auth status="0"/><Read status="0"><Invoice><id>1</id><number>234</number><customerid>204</customerid><total>99.00</total></Invoice></Read></response>'

json_string = utilities.xml2json(xml_res, strip=True)
print(json_string)
>>> '{"response": {"Read": {"@status": "0", "Invoice": {"total": "99.00", "id": "1", "customerid": "204", "number": "234"}}, "Auth": {"@status": "0"}}}'

json_obj = json.loads(json_string)
print(json_obj)
>>> {u'response': {u'Read': {u'@status': u'0', u'Invoice': {u'total': u'99.00', u'number': u'234', u'id': u'1', u'customerid': u'204'}}, u'Auth': {u'@status': u'0'}}}

print(json_obj['response']['Read']['@status'])
>>> '0'

print(json_obj['response']['Read']['Invoice']['total'])
>>> '99.00'
```