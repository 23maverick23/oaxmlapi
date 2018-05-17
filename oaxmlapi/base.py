# -*- coding: utf-8
"""The base class has helper methods for often used functions.
"""

from __future__ import absolute_import
from xml.dom import minidom

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class _Base(object):
    """
    A base class for defining helpful class methods.

    """
    def __init__(self):
        self._header = False

    def __str__(self):
        return "<_Base>"

    def _main(self):
        return None

    def tostring(self):
        """
        Return a bytestring containing XML tags.

        """
        header, body = None, None

        if self._header:
            header = b'<?xml version="1.0" encoding="utf-8"?>'

        if self._main() is not None:
            body = ET.tostring(self._main(), 'utf-8')

        return (header if header else b'') + (body if body else b'')

    def prettify(self):
        """
        Return a formatted, prettified string containing XML tags. Note
        that this also adds an XML declaration tag to the top of the XML
        document, so this should only be used for debugging.

        """
        reparsed = minidom.parseString(self.tostring())
        return reparsed.toprettyxml(indent='  ', encoding='utf-8')
