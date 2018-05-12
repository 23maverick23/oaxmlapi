---
description: The datatypes.py module is used to generate XML API datatype objects and tags.
---

# Datatypes

## Datatype

Use the Datatype method to create XML objects using the _ElementTree_ library.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| fields | Object | a dictionary of key[value] pairs |

### getDatatype

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

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
print my_date.tostring()
>>> '<Date><hour>08</hour><month>03</month><second>43</second><year>2012</year><day>14</day><minute>35</minute></Date>'

print my_date.prettify()
>>> '''
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