# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET



class TestReportClass(unittest.TestCase):

    def test_str(self):
        report = datatypes.Datatype(
            'Timesheet',
            {
                'relatedid': '1286',
                'email_report': '1'
            }
        )
        self.assertEqual(
            str(commands.Report('Timesheet', report)),
            '<Report type=Timesheet>'
        )

    def test_report(self):
        report = datatypes.Datatype(
            'Timesheet',
            {
                'relatedid': '1286',
                'email_report': '1'
            }
        )
        self.assertIsInstance(
            commands.Report('Timesheet', report).getReport(),
            ET.Element
        )

    def test_tostring(self):
        report = datatypes.Datatype(
            'Timesheet',
            {
                'relatedid': '1286',
                'email_report': '1'
            }
        )
        self.assertEqual(
            commands.Report('Timesheet', report).tostring(),
            (
                b'<Report type="Timesheet"><Timesheet><relatedid>1286</relatedid>'
                b'<email_report>1</email_report></Timesheet></Report>'
            )
        )

    def test_prettify(self):
        report = datatypes.Datatype(
            'Timesheet',
            {
                'relatedid': '1286',
                'email_report': '1'
            }
        )
        self.assertEqual(
            commands.Report('Timesheet', report).prettify(),
            b'<?xml version="1.0" encoding="utf-8"?>\n'
            b'<Report type="Timesheet">\n'
            b'  <Timesheet>\n'
            b'    <relatedid>1286</relatedid>\n'
            b'    <email_report>1</email_report>\n'
            b'  </Timesheet>\n'
            b'</Report>\n'
        )

    def test_invalid_type(self):
        with self.assertRaises(Exception):
            invoice = datatypes.Datatype(
                'Invoice',
                {
                    'relatedid': '1286',
                    'email_report': '1'
                }
            )
            commands.Report('Invoice', invoice)

suite = unittest.TestLoader().loadTestsFromTestCase(TestReportClass)
unittest.TextTestRunner(verbosity=2).run(suite)
