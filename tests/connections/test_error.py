# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import connections

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestErrorClass(unittest.TestCase):

    def test_str(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        error = connections.Error(app, '201')
        self.assertEqual(
            str(connections.Error(app, '201')),
            '<Error code=201>'
        )

    def test_error(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        self.assertIsInstance(
            connections.Error(app, '201').error(),
            ET.Element
        )

    def test_tostring(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        self.assertEqual(
            connections.Error(app, '201').tostring(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>'
                b'<request API_ver="1.0" client="test" client_ver="1.0" '
                b'key="abc123" namespace="default"><Read method="equal to" '
                b'type="Error"><Error><code>201</code></Error></Read>'
                b'</request>'
            )
        )

    def test_prettify(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        self.assertEqual(
            connections.Error(app, '201').prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<request API_ver="1.0" client="test" client_ver="1.0" key="abc123" namespace="default">\n'
                b'  <Read method="equal to" type="Error">\n'
                b'    <Error>\n'
                b'      <code>201</code>\n'
                b'    </Error>\n'
                b'  </Read>\n'
                b'</request>\n'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestErrorClass)
unittest.TextTestRunner(verbosity=2).run(suite)
