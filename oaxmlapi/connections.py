# -*- coding: utf-8

from __future__ import absolute_import
from xml.dom import minidom

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


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
        remoteAuth = ET.Element('RemoteAuth')
        login = ET.SubElement(remoteAuth, 'Login')

        company = ET.Element('company')
        company.text = self.company

        username = ET.Element('user')
        username.text = self.username

        password = ET.Element('password')
        password.text = self.password

        login.append(company)
        login.append(username)
        login.append(password)
        return remoteAuth

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


class MakeURL(object):
    """
    Use the MakeURL command to obtain a URL for a specific application page.

    Arguments:
        uid (str): a user id string
        page (str): a page name string
        app (str): an app string
        arg (obj): a Datatype object

    """
    def __init__(self, uid, page, app, arg):
        self.uid = uid
        self.page = page
        self.app = app
        self.arg = arg

    def __str__(self):
        return "%s (%s)" % (self.page, self.app)

    def makeurl(self):
        """
        Returns an ElementTree object containing an XML MakeURL tag.

        """
        makeurl = ET.Element('MakeURL')

        uid = ET.Element('uid')
        uid.text = self.uid

        page = ET.Element('page')
        page.text = self.page

        app = ET.Element('app')
        app.text = self.app

        if self.arg:
            arg = ET.Element('arg')
            arg.append(self.arg.getDatatype())
            makeurl.append(arg)

        makeurl.append(uid)
        makeurl.append(page)
        makeurl.append(app)
        return makeurl

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.makeurl(), 'utf-8')

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
        if isinstance(self.datatype, Datatype):
            whoami.append(self.datatype.getDatatype())
        elif isinstance(self.datatype, Auth):
            whoami.append(self.datatype.auth())
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
        request.append(self.auth.auth())

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


class Error(object):
    """
    Use the Error command to return info about an error code.
    Fetching errors does not require authentication, so this is 
    a shortcut without having to create a Datatype and Read
    command separatey.

    Arguments:
        code (str): an error code string

    """
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return "Error code %s" % self.code

    def error(self):
        """
        Returns an ElementTree object containing XML error tags.

        """
        request = ET.Element('request')
        read = ET.SubElement(request, 'Read')
        read.attrib = {'type': 'Error', 'method': 'equal to'}
        error = ET.SubElement(read, 'Error')
        code = ET.SubElement(error, 'code')
        code.text = self.code
        return request

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.error(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')
