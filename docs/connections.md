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
print(app.client)
>>> b'test app'
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

```python
auth = connections.Auth('My Company', 'JAdmin', 'p@ssw0rd')
print(auth.username)
>>> b'JAdmin'

print(auth.tostring())
>>> b'<Auth><Login><company>My Company</company><user>JAdmin</user><password>p@ssw0rd</password></Login></Auth>'
```

> Supports `tostring()` and `prettify()`.

## RemoteAuth

Stores authentication specific information needed for the remote auth tag.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| company | String | the company ID for login |
| username | String | the user ID for login |
| password | String | the password for login |

### remoteauth

Returns an _ElementTree_ object.

```python
# remoteauth acts exactly like auth
print(remoteauth.tostring())
>>> b'<RemoteAuth><Login><company>My Company</company><user>JAdmin</user><password>p@ssw0rd</password></Login></RemoteAuth>'
```

> Supports `tostring()` and `prettify()`.

## Whoami

The Whoami command returns information about the currently authenticated user. It is the equivalent of using the Read command for User.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| datatype | Datatype \| Auth | a datatype.Datatpe or connections.Auth object |

### whoami

Returns an _ElementTree_ object.

```python
user = datatypes.Datatype('User', {'id': '1234'})
xml_data = connections.Whoami(user)
print(xml_data.tostring())
>>> b'<Whoami><User><id>1234</id></User></Whoami>'
```

> Supports `tostring()` and `prettify()`.

## Request

The Request command returns a complete API request object in the correct format.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| application | Datatype | a connections.Application object |
| credentials | Datatype | a connections.Auth object |
| xml\_data | List | a list of _ElementTree_ objects |

### request

Returns an _ElementTree_ object.

```python
req = connections.Request(app, auth, xml_data)
print(req.tostring())
>>> b'<?xml version="1.0" encoding="utf-8"self._header?><request API_ver="1.0" client="test app" client_ver="1.0" key="uniquekey" namespace="default"><Auth><Login><company>company_id</company><user>username</user><password>p@ssw0rd</password></Login></Auth>...</request>'
```

> Supports `tostring()` and `prettify()`.

## Error

The Error command reads an error code and returns information about it.

| **attribute** | **type** | **description** |
| --- | --- | --- |
| application | Datatype | a connections.Application object |
| code | String | an API error code |

### error

Returns an _ElementTree_ object.

```python
app = connections.Application('test app', '1.0', 'default', 'uniquekey')
error = connections.Error(app, '201')
print(error.tostring())
>>> b'<?xml version="1.0" encoding="utf-8"self._header?><request API_ver="1.0" client="test app" client_ver="1.0" key="uniquekey" namespace="default"><Read type="Error" method="equal to"><Error><code>201</code></Error></Read></request>'
```

> Supports `tostring()` and `prettify()`.
