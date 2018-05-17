# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestMakeUrlClass(unittest.TestCase):

    def test_str(self):
        timesheet = datatypes.Datatype('Timesheet', {'id': '1245'})
        self.assertEqual(
            str(commands.MakeURL('1', 'grid-timesheet', 'ta', timesheet)),
            '<MakeURL page=grid-timesheet app=ta>'
        )

    def test_makeurl(self):
        timesheet = datatypes.Datatype('Timesheet', {'id': '1245'})
        self.assertIsInstance(
            commands.MakeURL('1', 'grid-timesheet', 'ta', timesheet).makeurl(),
            ET.Element
        )

    def test_tostring_no_arg(self):
        self.assertEqual(
            commands.MakeURL('1', 'currency-rates', 'ma', {}).tostring(),
            (
                b'<MakeURL><uid>1</uid><page>currency-rates</page><app>ma</app></MakeURL>'
            )
        )

    def test_tostring_arg(self):
        timesheet = datatypes.Datatype('Timesheet', {'id': '1245'})
        self.assertEqual(
            commands.MakeURL('1', 'grid-timesheet', 'ta', timesheet).tostring(),
            (
                b'<MakeURL><arg><Timesheet><id>1245</id></Timesheet></arg>'
                b'<uid>1</uid><page>grid-timesheet</page><app>ta</app></MakeURL>'
            )
        )

    def test_prettify(self):
        timesheet = datatypes.Datatype('Timesheet', {'id': '1245'})
        self.assertEqual(
            commands.MakeURL('1', 'grid-timesheet', 'ta', timesheet).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<MakeURL>\n'
                b'  <arg>\n'
                b'    <Timesheet>\n'
                b'      <id>1245</id>\n'
                b'    </Timesheet>\n'
                b'  </arg>\n'
                b'  <uid>1</uid>\n'
                b'  <page>grid-timesheet</page>\n'
                b'  <app>ta</app>\n'
                b'</MakeURL>\n'
            )
        )

    def test_invalid_page(self):
        timesheet = datatypes.Datatype('Timesheet', {'id': '1245'})
        with self.assertRaises(Exception):
            commands.MakeURL('1', 'timesheet-entry', 'ta', timesheet).makeurl()

    def test_invalid_app(self):
        timesheet = datatypes.Datatype('Timesheet', {'id': '1245'})
        with self.assertRaises(Exception):
            commands.MakeURL('1', 'grid-timesheet', 'zz', timesheet).makeurl()

suite = unittest.TestLoader().loadTestsFromTestCase(TestMakeUrlClass)
unittest.TextTestRunner(verbosity=2).run(suite)
