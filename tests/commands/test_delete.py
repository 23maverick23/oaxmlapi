# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestDeleteClass(unittest.TestCase):

    def test_str(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        self.assertEqual(
            str(commands.Delete('Slip', slip)),
            '<Delete type=Slip>'
        )

    def test_delete(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        self.assertIsInstance(
            commands.Delete('Slip', slip).delete(),
            ET.Element
        )

    def test_tostring(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        self.assertEqual(
            commands.Delete('Slip', slip).tostring(),
            b'<Delete type="Slip"><Slip><id>1234</id></Slip></Delete>'
        )

    def test_prettify(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        self.assertEqual(
            commands.Delete('Slip', slip).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<Delete type="Slip">\n'
                b'  <Slip>\n'
                b'    <id>1234</id>\n'
                b'  </Slip>\n'
                b'</Delete>\n'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestDeleteClass)
unittest.TextTestRunner(verbosity=2).run(suite)
