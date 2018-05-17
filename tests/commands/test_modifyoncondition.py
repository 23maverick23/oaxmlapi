# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestModifyOnConditionClass(unittest.TestCase):

    def test_str(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        date = datatypes.Datatype(
            'Date',
            {'year': '2012'}
        )
        self.assertEqual(
            str(commands.ModifyOnCondition('Slip', slip, date)),
            '<ModifyOnCondition type=Slip>'
        )

    def test_modifyoncondition(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        date = datatypes.Datatype(
            'Date',
            {'year': '2012'}
        )
        self.assertIsInstance(
            commands.ModifyOnCondition('Slip', slip, date).modify(),
            ET.Element
        )

    def test_tostring(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        date = datatypes.Datatype(
            'Date',
            {'year': '2012'}
        )
        self.assertEqual(
            commands.ModifyOnCondition('Slip', slip, date).tostring(),
            (
                b'<ModifyOnCondition condition="if-not-updated" type="Slip">'
                b'<Slip><id>1234</id></Slip><Date><year>2012</year></Date>'
                b'</ModifyOnCondition>'
            )
        )

    def test_prettify(self):
        slip = datatypes.Datatype(
            'Slip',
            {'id': '1234'}
        )
        date = datatypes.Datatype(
            'Date',
            {'year': '2012'}
        )
        self.assertEqual(
            commands.ModifyOnCondition('Slip', slip, date).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<ModifyOnCondition condition="if-not-updated" type="Slip">\n'
                b'  <Slip>\n'
                b'    <id>1234</id>\n'
                b'  </Slip>\n'
                b'  <Date>\n'
                b'    <year>2012</year>\n'
                b'  </Date>\n'
                b'</ModifyOnCondition>\n'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestModifyOnConditionClass)
unittest.TextTestRunner(verbosity=2).run(suite)
