---
description: The commands.py module is used to generate XML API command tags.
---

# Commands

## Time

This command take no attributes and returns the current servertime.

### time

Returns an _ElementTree_ object.

```python
print(commands.Time().tostring())
>>> b'<Time/>'
```

> Supports `tostring()` and `prettify()`.

## Read

This command is used to read objects.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| method | String | one of: all, equal to, not equal to, custom equal to, user, project, not exported |
| attribs | Dict | one of: limit, deleted, include\_flags_, _include\_nondeleted_, _with\_project\_only, base\_currency, generic, enable\_custom |
| filters | List | a list of Filter objects |
| orderby | Dict | keys: field, order (default 'asc') |
| fields | List | a list of field names |

### read

Returns an _ElementTree_ object.

```python
xml_data = commands.Read(
    'Slip',
    'all',
    {'limit': '0, 1000'},
    None,
    None,
    ['customerid', 'id', 'projectid']
).read()

print(xml_data)
>>> b'<Read limit="0, 1000" method="all" type="Slip"><_Return><customerid /><id /><projectid /></_Return></Read>'
```

> Supports `tostring()` and `prettify()`.

## Read.Filter

This command is used to create read filter objects.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| filter | String \| None | one of: open-envelopes, open-envelopes, approved-envelopes, rejected-envelopes, submitted-envelopes, nonreimbursed-envelopes, reimbursable-envelope, open-slips, approved-slips, open-timesheets, approved-timesheets, rejected-timesheets, submitted-timesheets, not-exported, approved-revenue-recognition-transactions |
| field | String \| None | a field name to filter on |
| datatype | Datatype | a datatype.Datatpe object |

### getFilter

Returns a dictionary containing filter data.

```python
date = datatypes.Datatype(
    'Date',
    {
        'month': '11',
        'day': '24',
        'year': '2013'
    }
)

slip = datatypes.Datatype(
    'Slip',
    {
        'customerid': '7',
        'projectid': '14'
    }
)

filter1 = commands.Read.Filter(
    'older-than',
    'date',
    date
).getFilter()

filter2 = commands.Read.Filter(
    None,
    None,
    slip
).getFilter()

xml_data = commands.Read(
    'Slip',
    'equal to',
    {'limit': '0, 1000'},
    [filter1, filter2],
    None,
    ['customerid', 'id', 'projectid']
).read()

print(xml_data)
>>> b'<Read field="date" filter="older-than" limit="0, 1000" method="equal to" type="Slip"><Date><year>2013</year><day>24</day><month>11</month></Date><Slip><projectid>14</projectid><customerid>7</customerid></Slip><_Return><customerid /><id /><projectid /></_Return></Read>'
```

## Report

Use the Report command to run a report and email a PDF copy of a Timesheet, Envelope \(Exp Report\), or Saved report.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| report | Datatype | a datatype.Datatype object; one of Timesheet, Envelope, or Report |

### getReport

Returns an _ElementTree_ object.

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
print(xml_data.tostring())
>>> b'<Report type="Timesheet"><Timesheet><relatedid>1286</relatedid><email_report>1</email_report></Timesheet></Report>'
```

> Supports `tostring()` and `prettify()`.

## Add

Use the Add command to add records.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| attribs | Dict | one of: enable\_custom |
| datatype | Datatype | a datatype.Datatpe object |

### add

Returns an _ElementTree_ object.

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
print(xml_data.tostring())
>>> b'<Add type="Project"><Project><start_date><Date><year>2013</year><day>10</day><month>06</month></Date></start_date><userid>1</userid><name>New project</name><customerid>7</customerid></Project></Add>'
```

> Supports `tostring()` and `prettify()`.

## Delete

Use the Delete command to delete records.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| datatype | Datatype | a datatype.Datatpe object |

### delete

Returns an _ElementTree_ object.

```python
slip = datatypes.Datatype(
    'Slip',
    {'id': '1428'}
)
xml_data = commands.Delete('Slip', slip)
print(xml_data.tostring())
>>> b'<Delete type="Slip"><Slip><id>1428</id></Slip></Delete>'
```

> Supports `tostring()` and `prettify()`.

## Modify

Use the Modify command to modify records.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| attribs | Dict | one of: enable\_custom |
| datatype | Datatype | a datatype.Datatpe object |

### modify

Returns an _ElementTree_ object.

```python
# create datatype object for modifying a record
invoice = datatypes.Datatype(
    'Invoice',
    {'id': '476'}
)

# create modify object
xml_data = commands.Modify('Invoice', {}, invoice)
print(xml_data.tostring())
>>> b'<Modify type="Invoice"><Invoice><id>476</id></Invoice></Modify>'
```

> Supports `tostring()` and `prettify()`.

## ModifyOnCondition

Use the ModifyOnCondition command to perform actions such as updating the external_id of a record type only if the update time on the OpenAir server is older.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| datatype1 | Datatype | a datatype.Datatpe object |
| datatype2 | Datatype | a datatype.Datatpe object |

### modify

Returns an _ElementTree_ object.

```python
# create datatype object for modifying a record
invoice = datatypes.Datatype(
    'Invoice',
    {'id': '476', 'external_id': '123456789'}
)

date = datatypes.Datatype(
    'Date',
    {'month': '03', 'day': '14', 'year': '2012', 'hour': '08', 'minute': '35', 'second': '43'}
)

# create modifyoncondition object
xml_data = commands.ModifyOnCondition('Invoice', invoice, date)
print(xml_data.tostring())
>>> b'<ModifyOnCondition condition="if-not-updated" type="Invoice"><Invoice><id>476</id><external_id>123456789</external_id></Invoice><Date><hour>08</hour><month>03</month><second>43</second><year>2012</year><day>14</day><minute>35</minute></Date></ModifyOnCondition>'
```

> Supports `tostring()` and `prettify()`.

## Submit

Use the Submit command to submit records for approval.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| datatype | Datatype | a datatype.Datatpe object |
| approval | Datatype | a datatype.Datatpe object |

### submit

Returns an _ElementTree_ object.

```python
# create datatype object to submit
timesheet = datatypes.Datatype(
    'Timesheet',
    {'id': '476'}
)

# create datatype object for approval
approval = datatypes.Datatype(
    'Approval',
    {'cc': 'name@company.com', 'notes': 'submit notes'}
)

# create submit object
xml_data = commands.Submit('Timesheet', timesheet, approval)
print(xml_data.tostring())
>>> b'<Submit type="Timesheet"><Timesheet><id>476</id></Timesheet><Approval><cc>name@company.com</cc><notes>submit notes</notes></Approval></Submit>'
```

> Supports `tostring()` and `prettify()`.

## CreateAccount

Use the CreateAccount command to create a new OpenAir account.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| company | Datatype | a datatype.Datatpe object |
| user | Datatype | a datatype.Datatpe object |

### create

Returns an _ElementTree_ object.

```python
# create datatype object for company
company = datatypes.Datatype(
    'Company',
    {'nickname': 'New Account'}
)

# create datatype object for user
user = datatypes.Datatype(
    'User',
    {'nickname': 'JAdmin', 'password': 'p@ssw0rd', 'email': 'jadmin@company.com'}
)

# create createaccount object
xml_data = commands.CreateAccount(company, user)
print(xml_data.tostring())
>>> b'<CreateAccount><Company><nickname>New Account</nickname></Company><User><password>p@ssw0rd</password><nickname>JAdmin</nickname><addr><Address><email>jadmin@company.com</email></Address></addr></User></CreateAccount>'
```

> Supports `tostring()` and `prettify()`.

## CreateUser

Use the CreateUser command to create a new OpenAir user.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| company | Datatype | a datatype.Datatpe object |
| user | Datatype | a datatype.Datatpe object |

### create

Returns an _ElementTree_ object.

```python
# CreateUser is identical to CreateAccount
xml_data = commands.CreateUser(company, user)
print(xml_data.tostring())
>>> b'<CreateUser><Company><nickname>New Account</nickname></Company><User><password>p@ssw0rd</password><nickname>JAdmin</nickname><addr><Address><email>jadmin@company.com</email></Address></addr></User></CreateUser>'
```

> Supports `tostring()` and `prettify()`.

## Switch

Use the Switch command to customize the appearance of the product using switches and settings.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| type | String | an OpenAir complex type |
| user | Datatype | a datatype.Datatpe object |

### switch

Returns an _ElementTree_ object.

```python
flag = datatypes.Datatype(
    'Flag',
    {'name': '_switch_name', 'setting': '1'}
)
xml_data = commands.Switch('User', flag)
print(xml_data.tostring())
>>> b'<User><flags><Flag><setting>1</setting><name>_switch_name</name></Flag></flags></User>'
```

> Supports `tostring()` and `prettify()`.

## MakeURL

Use the MakeURL command to obtain a URL for a specific application and screen.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| uid | String | the id of a valid logged in user |
| page | String | one of: default-url, company-settings, currency-rates, import-export, custom-fields, list-reports, list-customers, list-projects, list-prospects, list-resources, list-timesheets, create-timesheet, list-timebills, list-invoices, create-invoice, list-envelope-receipts, list-envelopes, create-envelope, create-envelope-receipt, dashboard, list-purchase-requests, quick-search-resources, custom-search-resources, view-invoice, dashboard-project, grid-timesheet, report-timesheet |
| app | String | one of: 'km', 'ma', 'pb', 'rm', 'pm', 'ta, 'te', or 'tb' |
| arg | Datatype | a datatype.Datatpe object |

### makeurl

Returns an _ElementTree_ object.

```python
timesheet = datatypes.Datatype('Timesheet', {'id': '1245'})
xml_data = commands.MakeURL('1', 'grid-timesheet', 'ta', timesheet)
print(xml_data.tostring())
>>> b'<MakeURL><arg><Timesheet><id>1245</id></Timesheet></arg><uid>1</uid><page>grid-timesheet</page><app>ta</app></MakeURL>'
```

> Supports `tostring()` and `prettify()`.
