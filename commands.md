---
description: The commands.py module is used to generate XML API command tags.
---

# Commands

## Time

This command take no attributes and returns the current servertime.

```python
print commands.Time().tostring()
>>> '<Time />'
```

### time

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

## Read

This command is used to read objects.

| **attribute** | **type** | **description** |
| --- | --- | --- | --- | --- | --- |
| type | String | an OpenAir complex type |
| method | String | one of: all, equal to, not equal to, custom equal to, user, project, not exported |
| attribs | Object | one of: limit, deleted, include\_flags_, _include\_nondeleted_, _with\_project\_only, base\_currency, generic, enable\_custom |
| filters | Array | a list of Filter objects |
| fields | Array | a list of field names |

### read

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

{% hint style="warning" %}
All attributes must be provided in the Read method. If an attribute doesn't apply, pass in an empty array/dictionary or None.
{% endhint %}

Example of a simple date object.

```python
date = datatypes.Datatype(
    'Date',
    {
        'month': '11',
        'day': '24',
        'year': '2013'
    }
)
```

Example of a simple slip \(charge\) object.

```python
slip = datatypes.Datatype(
    'Slip',
    {
        'customerid': '7',
        'projectid': '14'
    }
)
```

## Read.Filter

This command is used to create read filter objects.

| **attribute** | **type** | **description** |
| --- | --- | --- | --- |
| filter | String \| None | one of: open-envelopes, open-envelopes, approved-envelopes, rejected-envelopes, submitted-envelopes, nonreimbursed-envelopes, reimbursable-envelope, open-slips, approved-slips, open-timesheets, approved-timesheets, rejected-timesheets, submitted-timesheets, not-exported, approved-revenue-recognition-transactions |
| field | String \| None | a field name to filter on |
| datatype | Datatype | a datatype.Datatpe object |

{% hint style="warning" %}
The Filter method requires a Datatype object, so make sure you create one before referencing it in this method.
{% endhint %}

### getFilter

Returns a dictionary containing filter data.

Example of a date filter.

```python
filter1 = commands.Read.Filter(
    'older-than',
    'date',
    date
).getFilter()
```

Example of a slip \(charge\) filter.

```python
filter2 = commands.Read.Filter(
    None,
    None,
    slip
).getFilter()
```

To create your final Read, just pass your Filter objects to the Read method.

```python
xml_data = commands.Read(
    'Slip',
    'equal to',
    {'limit': '0, 1000'},
    [filter1, filter2],
    ['customerid', 'id', 'projectid']
).read()

print xml_data
>>> '<Read deleted="1" field="date" filter="older-than" limit="0, 1000" method="equal to" type="Slip"><Date><year>2013</year><day>24</day><month>11</month></Date><Slip><projectid>14</projectid><customerid>7</customerid></Slip><_Return><customerid /><id /><projectid /></_Return></Read>'
```

## Report

Use the Report command to run a report and email a PDF copy of a Timesheet, Envelope \(Exp Report\), or Saved report.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| report | Datatype | a datatype.Datatype object; one of Timesheet, Envelope, or Report |

### getReport

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

{% hint style="warning" %}
This command only supports three datatypes today: Timesheet, Envelope, or Report
{% endhint %}

Example usage.

```python
# create datatype object
report = datatypes.Datatype(
    'Timesheet',
    {
        'relatedid': '1286',
        'email_report': '1'
    }
)

# create report object
xml_data = commands.Report(
    'Timesheet',
    report
)
print xml_data.tostring()
>>> '<Report type="Timesheet"><Timesheet><relatedid>1286</relatedid><email_report>1</email_report></Timesheet></Report>'
```

## Add

Use the Add command to add records.

| **attribute** | **type** | **description** |
| --- | --- | --- | --- |
| type | String | an OpenAir complex type |
| attribs | Object | one of: enable\_custom |
| datatype | Datatype | a datatype.Datatpe object |

### add

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

```python
# create datatype object for adding a date record
date = datatypes.Datatype(
    'Date',
    {'month': '06', 'day': '10', 'year': '2013'}
)

# create datatype object for adding a record
project = datatypes.Datatype(
    'Project',
    {'name': 'New project', 'customerid': '7', 'userid': '1', 'start_date': date}
)

# create add object
xml_data = commands.Add('Project', {}, project)
print xml_data.tostring()
>>> '<Add type="Project"><Project><start_date><Date><year>2013</year><day>10</day><month>06</month></Date></start_date><userid>1</userid><name>New project</name><customerid>7</customerid></Project></Add>'
```

