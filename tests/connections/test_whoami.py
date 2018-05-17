# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import connections, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestWhoamiClass(unittest.TestCase):

    def test_str(self):
        user = datatypes.Datatype('User', {'id': '1234'})
        self.assertEqual(
            str(connections.Whoami(user)),
            '<Whoami>'
        )

    def test_whoami(self):
        user = datatypes.Datatype('User', {'id': '1234'})
        self.assertIsInstance(
            connections.Whoami(user).whoami(),
            ET.Element
        )

    def test_whoami_nondatatype(self):
        user = datatypes.Datatype('User', {'id': '1234'}).tostring()
        with self.assertRaises(Exception):
            connections.Whoami(user)

    def test_whoami_nonuser(self):
        customer = datatypes.Datatype('Customer', {'id': '1234'})
        with self.assertRaises(Exception):
            connections.Whoami(customer)

    def test_tostring_user(self):
        user = datatypes.Datatype('User', {'id': '1234'})
        self.assertEqual(
            connections.Whoami(user).tostring(),
            b'<Whoami><User><id>1234</id></User></Whoami>'
        )

    def test_prettify(self):
        user = datatypes.Datatype('User', {'id': '1234'})
        self.assertEqual(
            connections.Whoami(user).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<Whoami>\n'
                b'  <User>\n'
                b'    <id>1234</id>\n'
                b'  </User>\n'
                b'</Whoami>\n'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestWhoamiClass)
unittest.TextTestRunner(verbosity=2).run(suite)
