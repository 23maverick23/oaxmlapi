---
description: The datatypes.py module is used to generate XML API datatype objects and tags.
---

# Datatypes

## Datatype

Use the Datatype method to create XML objects using the _ElementTree_ library.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| fields | Dict | a dictionary of key[value] pairs |

### getDatatype

Returns an _ElementTree_ object.

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

> Supports `tostring()` and `prettify()`.