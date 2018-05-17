# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestSubmitClass(unittest.TestCase):

    def test_str(self):
        timesheet = datatypes.Datatype(
            'Timesheet',
            {'id': '476'}
        )
        approval = datatypes.Datatype(
            'Approval',
            {}
        )
        self.assertEqual(
            str(commands.Submit('Timesheet', timesheet, approval)),
            '<Submit type=Timesheet>'
        )

    def test_submit(self):
        timesheet = datatypes.Datatype(
            'Timesheet',
            {'id': '476'}
        )
        approval = datatypes.Datatype(
            'Approval',
            {}
        )
        self.assertIsInstance(
            commands.Submit('Timesheet', timesheet, approval).submit(),
            ET.Element
        )

    def test_tostring(self):
        timesheet = datatypes.Datatype(
            'Timesheet',
            {'id': '476'}
        )
        approval = datatypes.Datatype(
            'Approval',
            {}
        )
        self.assertEqual(
            commands.Submit('Timesheet', timesheet, approval).tostring(),
            (
                b'<Submit type="Timesheet"><Timesheet><id>476</id>'
                b'</Timesheet><Approval /></Submit>'
            )
        )

    def test_prettify(self):
        timesheet = datatypes.Datatype(
            'Timesheet',
            {'id': '476'}
        )
        approval = datatypes.Datatype(
            'Approval',
            {}
        )
        self.assertEqual(
            commands.Submit('Timesheet', timesheet, approval).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<Submit type="Timesheet">\n'
                b'  <Timesheet>\n'
                b'    <id>476</id>\n'
                b'  </Timesheet>\n'
                b'  <Approval/>\n'
                b'</Submit>\n'
            )
        )

    def test_invalid_method(self):
        booking = datatypes.Datatype(
            'Booking',
            {'id': '476'}
        )
        approval = datatypes.Datatype(
            'Approval',
            {}
        )
        with self.assertRaises(Exception):
            commands.Submit('Booking', booking, approval).submit()

suite = unittest.TestLoader().loadTestsFromTestCase(TestSubmitClass)
unittest.TextTestRunner(verbosity=2).run(suite)
