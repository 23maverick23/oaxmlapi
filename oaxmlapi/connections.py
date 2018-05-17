# -*- coding: utf-8
"""The connections.py module allows for the creation of an app
which will contain required information for the API. It also
allows for the storage of login information for authentication.
"""

from __future__ import absolute_import, print_function

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from oaxmlapi.base import _Base
from oaxmlapi.datatypes import Datatype


class Application(object):
    """
    Use the Application command to collect application information.

    Arguments:
        client (str): a client string
        client_version (str): a client_version string
        namespace (str): a namespace string
        key (str): a key string

    """
    def __init__(self, client, client_version, namespace, key):
        self.client = client
        self.client_version = client_version
        self.namespace = namespace
        self.key = key

    def __str__(self):
        return "<Application client={client} version={version}>".format(
            client=self.client, version=self.client_version)


class Auth(_Base):
    """
    Use the Auth command to collect authentication information.

    Arguments:
        company (str): a company string
        username (str): a username string
        password (str): a password string

    """
    def __init__(self, company, username, password):
        _Base.__init__(self)
        self.company = company
        self.username = username
        self.password = password

    def __str__(self):
        return "<Auth company={company} username={username}>".format(
            company=self.company, username=self.username)

    def auth(self):
        """
        Returns an ElementTree object containing an XML Auth tag.

        """
        auth = ET.Element('Auth')
        login = ET.SubElement(auth, 'Login')

        company = ET.Element('company')
        company.text = self.company

        username = ET.Element('user')
        username.text = self.username

        password = ET.Element('password')
        password.text = self.password

        login.append(company)
        login.append(username)
        login.append(password)
        return auth

    def _main(self):
        return self.auth()


class RemoteAuth(_Base):
    """
    Use the RemoteAuth command to log in to an individual user account.

    Arguments:
        company (str): a company string
        username (str): a username string
        password (str): a password string

    """
    def __init__(self, company, username, password):
        _Base.__init__(self)
        self.company = company
        self.username = username
        self.password = password

    def __str__(self):
        return "<RemoteAuth company={company} username={username}>".format(
            company=self.company, username=self.username)

    def remoteauth(self):
        """
        Returns an ElementTree object containing an XML RemoteAuth tag.

        """
        remoteauth = ET.Element('RemoteAuth')
        login = ET.SubElement(remoteauth, 'Login')

        company = ET.Element('company')
        company.text = self.company

        username = ET.Element('user')
        username.text = self.username

        password = ET.Element('password')
        password.text = self.password

        login.append(company)
        login.append(username)
        login.append(password)
        return remoteauth

    def _main(self):
        return self.remoteauth()


class Whoami(_Base):
    """
    Use the Whoami command to return info about the authenticated user.

    Arguments:
        datatype (obj): a Datatype object

    """
    def __init__(self, datatype):
        _Base.__init__(self)
        self.datatype = datatype

    def __str__(self):
        return "<Whoami>"

    @property
    def datatype(self):
        return self._datatype

    @datatype.setter
    def datatype(self, d):
        if not isinstance(d, Datatype):
            raise Exception('you must pass a Datatype object')
        elif not d.type == 'User':
            raise Exception('you must pass a User Datatype not "{type}"').format(
                type=d.type
            )
        self._datatype = d

    def whoami(self):
        """
        Returns an ElementTree object containing an XML Whoami tag.

        """
        whoami = ET.Element('Whoami')
        whoami.append(self.datatype.getDatatype())
        return whoami

    def _main(self):
        return self.whoami()


class Request(_Base):
    """
    Use the Request command to create a complete XML request with tags.

    Arguments:
        application (obj): an Application object
        auth (obj): an Auth object
        xml_data (list): a list of Datatype object

    """
    def __init__(self, application, auth, xml_data):
        _Base.__init__(self)
        self.application = application
        self.auth = auth
        self.xml_data = xml_data
        self._header = True

    def __str__(self):
        return '<Request client={client} company={company} username={username}>'.format(
            client=self.application.client, company=self.auth.company,
            username=self.auth.username)

    def request(self):
        """
        Returns an ElementTree object containing an XML request tag
        and associated XML data.

        """
        request = ET.Element('request')
        request.attrib = {
            'API_ver': '1.0',
            'client': self.application.client,
            'client_ver': self.application.client_version,
            'namespace': self.application.namespace,
            'key': self.application.key
        }

        if isinstance(self.auth, Auth):
            request.append(self.auth.auth())
        elif isinstance(self.auth, RemoteAuth):
            request.append(self.auth.remoteauth())
        else:
            raise Exception('you must pass an Auth or RemoteAuth instance')

        if self.xml_data:
            for elem in self.xml_data:
                request.append(elem)

        return request

    def _main(self):
        return self.request()

class Error(_Base):
    """
    Use the Error command to return info about an error code.
    Fetching errors does not require authentication, so this is
    a shortcut without having to create a Datatype and Read
    command separately.

    Arguments:
        code (str): an error code string

    """
    def __init__(self, application, code):
        _Base.__init__(self)
        self.application = application
        self.code = str(code)
        self._header = True

    def __str__(self):
        return "<Error code={code}>".format(code=self.code)

    def error(self):
        """
        Returns an ElementTree object containing XML error tags.

        """
        request = ET.Element('request')
        request.attrib = {
            'API_ver': '1.0',
            'client': self.application.client,
            'client_ver': self.application.client_version,
            'namespace': self.application.namespace,
            'key': self.application.key
        }

        read = ET.SubElement(request, 'Read')
        read.attrib = {'type': 'Error', 'method': 'equal to'}

        error = ET.SubElement(read, 'Error')
        code = ET.SubElement(error, 'code')
        code.text = self.code
        return request

    def _main(self):
        return self.error()
