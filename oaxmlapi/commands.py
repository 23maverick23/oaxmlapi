# -*- coding: utf-8

from __future__ import absolute_import
from xml.dom import minidom

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class Time(object):
    """
    The Time command returns the current time on our servers.

    Arguments:
        none

    """
    def __init__(self):
        pass

    def __str__(self):
        return "time object"

    def time(self):
        """
        Returns an ElementTree object containing a time tag.

        """
        return ET.Element('Time')

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.time(), 'utf-8')


class Read(object):
    """
    Use the read command to retrieve data from OpenAir.

    Arguments:
        type (str): a valid XML type
        method (str): a valid read method
        attribs (dict): a dictionary containing read attributes
        filters (list): a list of filter types
        return_fields (list): a list of fields to return

    """
    def __init__(self, type, method, attribs, filters, fields):
        self.type = type
        self.method = method
        self.attribs = attribs
        self.filters = filters
        self.fields = fields

    def __str__(self):
        return "%s (method: %s)" % (self.type, self.method, )

    def read(self):
        """
        Returns an ElementTree object containing a read tag,
        as well as all the appropriate attributes and filters.

        """
        elem = ET.Element('Read')
        attribs = {}
        attribs['type'] = self.type
        attribs['method'] = self.method

        # process all read attributes
        for key in self.attribs:
            attribs[key] = self.attribs[key]

        # create filter information
        if self.filters:
            filter_list = []
            field_list = []

            for item in self.filters:
                if item['filter']:
                    filter_list.append(item['filter'])
                elif item['datatype']:
                    elem.append(item['datatype'])

                if item['fieldname']:
                    field_list.append(item['fieldname'])
                    elem.append(item['datatype'])

            if field_list:
                attribs['field'] = ','.join(field_list)

            if filter_list:
                attribs['filter'] = ','.join(filter_list)

        # add all attribs to the XML element
        elem.attrib = attribs

        # process return fields
        if self.fields:
            subelem = ET.SubElement(elem, '_Return')

            for f in self.fields:
                ET.SubElement(subelem, f)

        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.read(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')

    class Filter(object):
        """
        Creates a filter object for filtering read commands.

        Arguments:
            filter (str): the type of filter
            field (str): the field to be filtered
            datatype (obj): a valid XML element

        """
        def __init__(self, filter, fieldname, datatype):
            self.filter = filter
            self.fieldname = fieldname
            self.datatype = datatype.getDatatype()

        def __str__(self):
            return "filter object"

        def getFilter(self):
            """
            Returns a dictionary of filter criteria.

            """
            f = {}
            f['filter'] = self.filter
            f['fieldname'] = self.fieldname
            f['datatype'] = self.datatype
            return f


class Report(object):
    """
    Use the Report command to run a report and email a PDF copy
    of a Timesheet, Envelope, or Saved report.

    Arguments:
        type (str): a valid XML type. Only Timesheet, Envelope
                        or Reportf datatypes are allowed
        report (obj): a valid XML report element datatype

    """
    def __init__(self, type, report):
        self.type = type
        self.report = report.getDatatype()

    # type
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, t):
        if not t in ['Timesheet', 'Envelope', 'Reportf']:
            raise Exception('type "%s" not supported' % t)
        self._type = t

    def getReport(self):
        """
        Returns an ElementTree object containing report tags.

        """
        elem = ET.Element('Report')
        attribs = {}
        attribs['type'] = self.type
        elem.attrib = attribs
        elem.append(self.report)
        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.getReport(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class Add(object):
    """
    Use the Add command to add records.

    Arguments:
        type (str): a valid XML type
        attrib (dict): a dictionary containing add attributes
        datatype (obj): a valid Datatype() object

    """
    def __init__(self, type, attribs, datatype):
        self.type = type
        self.attribs = attribs
        self.datatype = datatype.getDatatype()

    def __str__(self):
        return 'Add "%s"' % self.type

    # type
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, t):
        if t == 'User':
            raise Exception(
                'datatype "%s" not supported - use CreateUser' % t
            )
        if t == 'Company':
            raise Exception(
                'datatype "%s" not supported - use CreateAccount' % t
            )
        self._type = t

    def add(self):
        """
        Returns an ElementTree object containing add tags.

        """
        elem = ET.Element('Add')
        attribs = {}
        attribs['type'] = self.type

        # process all add attributes
        for key in self.attribs:
            attribs[key] = self.attribs[key]

        elem.attrib = attribs
        elem.append(self.datatype)
        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.add(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class Delete(object):
    """
    Use the Delete command to delete records.

    Arguments:
        type (str): a valid XML type
        datatype (obj): a valid Datatype() object

    """
    def __init__(self, type, datatype):
        self.type = type
        self.datatype = datatype.getDatatype()

    def __str__(self):
        return 'Delete "%s"' % self.type

    def delete(self):
        """
        Returns an ElementTree object containing delete tags.

        """
        elem = ET.Element('Delete')
        attribs = {}
        attribs['type'] = self.type
        elem.attrib = attribs
        elem.append(self.datatype)
        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.delete(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class Modify(object):
    """
    Use the Modify command to change records.

    Arguments:
        type (str): a valid XML type
        attrib (dict): a dictionary containing modify attributes
        datatype (obj): a valid Datatype() object

    """
    def __init__(self, type, attribs, datatype):
        self.type = type
        self.attribs = attribs
        self.datatype = datatype.getDatatype()

    def __str__(self):
        return 'Modify "%s"' % self.type

    def modify(self):
        """
        Returns an ElementTree object containing modify tags.

        """
        elem = ET.Element('Modify')
        attribs = {}
        attribs['type'] = self.type

        # process all add attributes
        for key in self.attribs:
            attribs[key] = self.attribs[key]

        elem.attrib = attribs
        elem.append(self.datatype)
        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.modify(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class Submit(object):
    """
    Use the Submit command to submit records.

    Arguments:
        type (str): a valid XML type
        datatype (obj): a valid Datatype() object
        approval (obj): a valid approval Datatype() object

    """
    def __init__(self, type, datatype, approval):
        self.type = type
        self.datatype = datatype.getDatatype()
        self.approval = approval.getDatatype()

    def __str__(self):
        return 'Submit "%s"' % self.type

    # type
    @property
    def type(self):
        return self._datatype

    @type.setter
    def type(self, t):
        if not t in ['Timesheet', 'Envelope']:
            raise Exception('type "%s" not supported' % t)
        self._datatype = t

    def submit(self):
        """
        Returns an ElementTree object containing submit tags.

        """
        elem = ET.Element('Submit')
        attribs = {}
        attribs['type'] = self.type
        elem.attrib = attribs
        elem.append(self.datatype)
        elem.append(self.approval)
        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.submit(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class CreateAccount(object):
    """
    Use the CreateAccount command to create a new OpenAir account.
    When a new account is created, the first user is also created
    as the account administrator.

    Arguments:
        company (obj): a valid company Datatype() object
        user (obj): a valid user Datatype() object

    """
    def __init__(self, company, user):
        self.company = company
        self.user = user

    def __str__(self):
        return 'CreateAccount for "%s"' % self.company.fields['nickname']

    # company
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, c):
        if not 'nickname' in c.fields:
            raise Exception('"nickname" is a required Company field' % c)
        self._company = c

    # user
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, u):
        if (
            not 'nickname' in u.fields or
            not 'password' in u.fields or
            not 'email' in u.fields
        ):
            raise Exception(
                '"nickname, password and email" are required User fields' % u
            )
        self._user = u

    def create(self):
        """
        Returns an ElementTree object containing submit tags.

        """
        elem = ET.Element('CreateAccount')
        elem.append(self.company.getDatatype())
        elem.append(self.user.getDatatype())
        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.create(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class CreateUser(object):
    """
    Use the CreateUser command to create a new OpenAir user.

    Arguments:
        company (obj): a valid company Datatype() object
        user (obj): a valid user Datatype() object

    """
    def __init__(self, company, user):
        self.company = company
        self.user = user

    def __str__(self):
        return 'CreateUser "%s"' % self.user.fields['nickname']

    # company
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, c):
        if not 'nickname' in c.fields:
            raise Exception('"nickname" is a required Company field' % c)
        self._company = c

    # user
    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, u):
        if (
            not 'nickname' in u.fields or
            not 'password' in u.fields or
            not 'email' in u.fields
        ):
            raise Exception(
                '"nickname, password and email" are required User fields' % u
            )
        self._user = u

    def create(self):
        """
        Returns an ElementTree object containing submit tags.

        """
        elem = ET.Element('CreateUser')
        elem.append(self.company.getDatatype())
        elem.append(self.user.getDatatype())
        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.create(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')


class Switch(object):
    """
    Use the Switch command to set Company and User records.

    Arguments:
        type (str): a valid XML type
        datatype (obj): a valid flag Datatype object

    """
    def __init__(self, type, datatype):
        self.type = type
        self.datatype = datatype

    def __str__(self):
        return '%s flag for "%s"' % (self.type, self.datatype['name'])

    def switch(self):
        """
        Returns an ElementTree object containing a switch tag.

        """
        elem = ET.Element(self.type)
        flags = ET.SubElement(elem, 'flags')
        flags.append(self.datatype.getDatatype())
        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.switch(), 'utf-8')

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


class Error(object):
    """
    Use the Error command to return info about an error code.
    Fetching errors does not require authentication, so this is
    a shortcut without having to create a Datatype and Read
    command separately.

    Arguments:
        code (str): an error code string

    """
    def __init__(self, application, code):
        self.application = application
        self.code = code

    def __str__(self):
        return "Error code %s" % self.code

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

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        header = '<?xml version="1.0" encoding="utf-8" standalone="yes"?>'
        return header + ET.tostring(self.error(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')
