# -*- coding: utf-8
"""The datatypes.py module is used to generate XML API datatype
objects and tags.
"""

from __future__ import absolute_import, print_function

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

from oaxmlapi.base import _Base
from oaxmlapi.utilities import ADDRESS_FIELDS


class Datatype(_Base):
    """
    Use the type object to create an XML type.

    type (str): a valid XML type
    fields (dict): a dict containing fieldnames and data

    """
    def __init__(self, type, fields):
        _Base.__init__(self)
        self.type = type
        self.fields = fields

    def __str__(self):
        return '<Datatype type={type}>'.format(type=self.type)

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
                    if not address_set:  # pragma: no cover
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

    def _main(self):
        return self.getDatatype()
