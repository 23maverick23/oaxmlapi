# -*- coding: utf-8

from __future__ import absolute_import
from xml.dom import minidom
from oaxmlapi.utilities import ADDRESS_FIELDS

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class Datatype(object):
    """
    Use the type object to create an XML type.

    type (str): a valid XML type
    fields (dict): a dict containing fieldnames and data

    """
    def __init__(self, type, fields):
        self.type = type
        self.fields = fields

    def __str__(self):
        return '"%s" datatype object' % self.type

    def getDatatype(self):
        """
        Return an XML object using the ElementTree library.

        Arguments:
            none

        Returns:
            elem (obj): an <Element> object from the ElementTree library

        """
        elem = ET.Element(self.type)

        if self.type == 'Filter':
            elem.attrib = {'type': 'customer'}
            for key in self.fields:
                subelem = ET.SubElement(elem, key)
                subelem.text = self.fields[key]
        else:
            for key in self.fields:
                address_set = False
                if key in ADDRESS_FIELDS:
                    if not address_set:
                        addr = ET.SubElement(elem, 'addr')
                        address = ET.SubElement(addr, 'Address')
                        address_set = True
                    subelem = ET.SubElement(address, key)
                    subelem.text = self.fields[key]
                elif isinstance(self.fields[key], Datatype):
                    subelem = ET.SubElement(elem, key)
                    subelem.append(self.fields[key].getDatatype())
                else:
                    subelem = ET.SubElement(elem, key)
                    subelem.text = self.fields[key]
        return elem

    def tostring(self):
        """
        Return a string containing XML tags.

        """
        return ET.tostring(self.getDatatype(), 'utf-8')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')
