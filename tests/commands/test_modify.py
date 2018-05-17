# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestModifyClass(unittest.TestCase):

    def test_str(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        self.assertEqual(
            str(commands.Modify('Slip', {}, slip)),
            '<Modify type=Slip>'
        )

    def test_modify(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        self.assertIsInstance(
            commands.Modify('Slip', {}, slip).modify(),
            ET.Element
        )

    def test_tostring(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        self.assertEqual(
            commands.Modify('Slip', {'enable_custom': '1'}, slip).tostring(),
            b'<Modify enable_custom="1" type="Slip"><Slip><id>1234</id></Slip></Modify>'
        )

    def test_prettify(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        self.assertEqual(
            commands.Modify('Slip', {}, slip).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<Modify type="Slip">\n'
                b'  <Slip>\n'
                b'    <id>1234</id>\n'
                b'  </Slip>\n'
                b'</Modify>\n'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestModifyClass)
unittest.TextTestRunner(verbosity=2).run(suite)
