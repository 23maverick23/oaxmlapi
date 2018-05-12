---
description: The connections.py module allows for the creation of an app which will contain required information for the API. It also allows for the storage of login information for authentication.
---

# Connections

## Application

Stores application specific information needed for the request tag.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| client | String | the name of your application |
| client_version | String | the version of your application |
| namespace | String | the namespace of your API key (usually _default_) |
| key | String | your API key |

```python
app = connections.Application(
    'test app',
    '1.0',
    'default',
    'uniquekey'
)
print app.client
>>> 'test app'
```

## Auth

Stores authentication specific information needed for the auth tag.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| company | String | the company ID for login |
| username | String | the user ID for login |
| password | String | the password for login |

### auth

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

```python
auth = connections.Auth('My Company', 'JAdmin', 'p@ssw0rd')
print auth.username
>>> 'JAdmin'

print auth.tostring()
>>> '<Auth><Login><company>My Company</company><user>JAdmin</user><password>p@ssw0rd</password></Login></Auth>'
```

## RemoteAuth

Stores authentication specific information needed for the remote auth tag.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| company | String | the company ID for login |
| username | String | the user ID for login |
| password | String | the password for login |

### remoteauth

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

```python
# remoteauth acts exactly like auth
print remoteauth.tostring()
>>> '<RemoteAuth><Login><company>My Company</company><user>JAdmin</user><password>p@ssw0rd</password></Login></RemoteAuth>'
```

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

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

```python
timesheet = datatypes.Datatype('Timesheet', {'id': '1245'})
xml_data = connections.MakeURL('1', 'grid-timesheet', 'ta', timesheet)
print xml_data.tostring()
>>> '<MakeURL><arg><Timesheet><id>1245</id></Timesheet></arg><uid>1</uid><page>grid-timesheet</page><app>ta</app></MakeURL>'
```

## Whoami

The Whoami command returns information about the currently authenticated user. It is the equivalent of using the Read command for User.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| datatype | Datatype \| Auth | a datatype.Datatpe or connections.Auth object |

### whoami

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

```python
user = datatypes.Datatype('User', {'id': '1234'})
xml_data = connections.Whoami(user)
print xml_data.tostring()
>>> '<Whoami><User><id>1234</id></User></Whoami>'

# you can also pass in an Auth object
print connections.Whoami(connections.Auth('My Company', 'JAdmin', 'p@ssw0rd')).tostring()
>>> '<Whoami><Auth><Login><company>My Company</company><user>JAdmin</user><password>p@ssw0rd</password></Login></Auth></Whoami>'
```

## Request

The Request command returns a complete API request object in the correct format.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| application | Datatype | a connections.Application object |
| credentials | Datatype | a connections.Auth object |
| xml\_data | Array | an array of _ElementTree_ objects |

### request

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

```python
req = connections.Request(app, auth, xml_data)
print req.tostring()
>>> '<?xml version="1.0" encoding="utf-8" standalone="yes"?><request API_ver="1.0" client="test app" client_ver="1.0" key="uniquekey" namespace="default"><Auth><Login><company>company_id</company><user>username</user><password>p@ssw0rd</password></Login></Auth>...</request>'
```

## Error

The Error command reads an error code and returns information about it.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| application | Datatype | a connections.Application object |
| code | String | an API error code |

### error

Returns an _ElementTree_ object.

### tostring

Returns a string of XML tags.

### prettify

Return a formatted, prettified string containing XML tags.

```python
app = connections.Application('test app', '1.0', 'default', 'uniquekey')
error = connections.Error(app, '201')
print error.tostring()
>>> '<?xml version="1.0" encoding="utf-8" standalone="yes"?><request API_ver="1.0" client="test app" client_ver="1.0" key="uniquekey" namespace="default"><Read type="Error" method="equal to"><Error><code>201</code></Error></Read></request>'
```
