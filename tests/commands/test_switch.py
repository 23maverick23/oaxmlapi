# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestSwitchClass(unittest.TestCase):

    def test_str_user(self):
        flag = datatypes.Datatype(
            'Flag',
            {'setting': '1'}
        )
        self.assertEqual(
            str(commands.Switch('User', flag)),
            '<Switch type=User>'
        )

    def test_str_company(self):
        flag = datatypes.Datatype(
            'Flag',
            {'setting': '1'}
        )
        self.assertEqual(
            str(commands.Switch('Company', flag)),
            '<Switch type=Company>'
        )

    def test_submit(self):
        flag = datatypes.Datatype(
            'Flag',
            {'setting': '1'}
        )
        self.assertIsInstance(
            commands.Switch('User', flag).switch(),
            ET.Element
        )

    def test_tostring(self):
        flag = datatypes.Datatype(
            'Flag',
            {'setting': '1'}
        )
        self.assertEqual(
            commands.Switch('User', flag).tostring(),
            (
                b'<User><flags><Flag><setting>1</setting></Flag></flags></User>'
            )
        )

    def test_prettify(self):
        flag = datatypes.Datatype(
            'Flag',
            {'setting': '1'}
        )
        self.assertEqual(
            commands.Switch('User', flag).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<User>\n'
                b'  <flags>\n'
                b'    <Flag>\n'
                b'      <setting>1</setting>\n'
                b'    </Flag>\n'
                b'  </flags>\n'
                b'</User>\n'
            )
        )

    def test_invalid_method(self):
        flag = datatypes.Datatype(
            'Flag',
            {'setting': '1'}
        )
        with self.assertRaises(Exception):
            commands.Switch('Project', flag).switch()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSwitchClass)
unittest.TextTestRunner(verbosity=2).run(suite)
