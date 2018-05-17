# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import connections

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestRemoteAuthClass(unittest.TestCase):

    def test_str(self):
        self.assertEqual(
            str(connections.RemoteAuth('company', 'username', 'p@ssw0rd')),
            '<RemoteAuth company=company username=username>'
        )

    def test_auth(self):
        self.assertIsInstance(
            connections.RemoteAuth('company', 'username', 'p@ssw0rd').remoteauth(),
            ET.Element
        )

    def test_tostring(self):
        self.assertEqual(
            connections.RemoteAuth('company', 'username', 'p@ssw0rd').tostring(),
            (
            b'<RemoteAuth><Login><company>company</company><user>username</user>'
            b'<password>p@ssw0rd</password></Login></RemoteAuth>'
            )
        )

    def test_prettify(self):
        self.assertEqual(
            connections.RemoteAuth('company', 'username', 'p@ssw0rd').prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<RemoteAuth>\n'
                b'  <Login>\n'
                b'    <company>company</company>\n'
                b'    <user>username</user>\n'
                b'    <password>p@ssw0rd</password>\n'
                b'  </Login>\n'
                b'</RemoteAuth>\n'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoteAuthClass)
unittest.TextTestRunner(verbosity=2).run(suite)
