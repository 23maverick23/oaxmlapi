# -*- coding: utf-8

from __future__ import absolute_import
from xml.dom import minidom

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


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
        return "%s (v%s)" % (self.client, self.version)


class Auth(object):
    """
    Use the Auth command to collect authentication information.

    Arguments:
        company (str): a company string
        username (str): a username string
        password (str): a password string

    """
    def __init__(self, company, username, password):
        self.company = company
        self.username = username
        self.password = password

    def __str__(self):
        return "%s, %s, *****" % (self.company, self.username)

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

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.auth(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class RemoteAuth(object):
    """
    Use the RemoteAuth command to log in to an individual user account.

    Arguments:
        company (str): a company string
        username (str): a username string
        password (str): a password string

    """
    def __init__(self, company, username, password):
        self.company = company
        self.username = username
        self.password = password

    def __str__(self):
        return "%s, %s, *****" % (self.company, self.username)

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

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.remoteauth(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class Whoami(object):
    """
    Use the Whoami command to return info about the authenticated user.

    Arguments:
        datatype (obj): a Datatype object

    """
    def __init__(self, datatype):
        self.datatype = datatype

    def __str__(self):
        return "Whoami object"

    def whoami(self):
        """
        Returns an ElementTree object containing an XML Whoami tag.

        """
        from components.datatypes import Datatype

        whoami = ET.Element('Whoami')
        if isinstance(self.datatype, Datatype) and self.datatype.type == 'User':
            whoami.append(self.datatype.getDatatype())
        return whoami

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.whoami(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class Request(object):
    """
    Use the Request command to create a complete XML request with tags.

    Arguments:
        application (obj): an Application object
        auth (obj): an Auth object
        xml_data (list): a list of Datatype object

    """
    def __init__(self, application, auth, xml_data):
        self.application = application
        self.auth = auth
        self.xml_data = xml_data

    def __str__(self):
        return '"%s" request as %s\%s' % (
            self.application.client,
            self.auth.company,
            self.auth.username
        )

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

        if self.xml_data:
            for elem in self.xml_data:
                request.append(elem)

        return request

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        header = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>'
        return header + ET.tostring(self.request(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')
