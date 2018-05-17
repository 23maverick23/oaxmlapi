# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestReadClass(unittest.TestCase):

    def test_str(self):
        read = commands.Read(
            'Slip',
            'all',
            {'limit': '0, 1000'},
            None,
            None,
            ['id']
        )
        self.assertEqual(
            str(read),
            '<Read type=Slip method=all>'
        )

    def test_read(self):
        read = commands.Read(
            'Slip',
            'all',
            {'limit': '0, 1000'},
            None,
            None,
            ['id']
        )
        self.assertIsInstance(
            read.read(),
            ET.Element
        )

    def test_tostring_basic(self):
        read = commands.Read(
            'Slip',
            'all',
            {'limit': '0, 1000'},
            None,
            None,
            None
        )
        self.assertEqual(
            read.tostring(),
            b'<Read limit="0, 1000" method="all" type="Slip" />'
        )

    def test_tostring_filter_datatype(self):
        slip = datatypes.Datatype(
            'Slip',
            {
                'customerid': '7'
            }
        )
        filter1 = commands.Read.Filter(
            None,
            None,
            slip
        ).getFilter()
        read = commands.Read(
            'Slip',
            'equal to',
            {'limit': '0, 1000'},
            [filter1],
            None,
            None
        )
        self.assertEqual(
            read.tostring(),
            (
                b'<Read limit="0, 1000" method="equal to" type="Slip">'
                b'<Slip><customerid>7</customerid></Slip></Read>'
            )
        )

    def test_tostring_filter_field(self):
        date = datatypes.Datatype(
            'Date',
            {
                'year': '2013'
            }
        )
        filter1 = commands.Read.Filter(
            'older-than',
            'date',
            date
        ).getFilter()
        read = commands.Read(
            'Slip',
            'equal to',
            {'limit': '0, 1000'},
            [filter1],
            None,
            None
        )
        self.assertEqual(
            read.tostring(),
            (
                b'<Read field="date" filter="older-than" limit="0, 1000" '
                b'method="equal to" type="Slip"><Date><year>2013</year>'
                b'</Date></Read>'
            )
        )

    def test_tostring_orderby(self):
        read = commands.Read(
            'Slip',
            'all',
            {'limit': '0, 1000'},
            None,
            {'field': 'created', 'order': 'desc'},
            None
        )
        self.assertEqual(
            read.tostring(),
            (
                b'<Read limit="0, 1000" method="all" order="created,desc" type="Slip" />'
            )
        )

    def test_tostring_fields(self):
        read = commands.Read(
            'Slip',
            'all',
            {'limit': '0, 1000'},
            None,
            None,
            ['id']
        )
        self.assertEqual(
            read.tostring(),
            (
                b'<Read limit="0, 1000" method="all" type="Slip"><_Return>'
                b'<id /></_Return></Read>'
            )
        )

    def test_prettify(self):
        read = commands.Read(
            'Slip',
            'all',
            {'limit': '0, 1000'},
            None,
            None,
            ['id']
        )
        self.assertEqual(
            read.prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<Read limit="0, 1000" method="all" type="Slip">\n'
                b'  <_Return>\n'
                b'    <id/>\n'
                b'  </_Return>\n'
                b'</Read>\n'
            )
        )

    def test_invalid_method(self):
        with self.assertRaises(Exception):
            commands.Read(
                'Slip',
                'any',
                {'limit': '0, 1000'},
                None,
                None,
                None
            )

suite = unittest.TestLoader().loadTestsFromTestCase(TestReadClass)
unittest.TextTestRunner(verbosity=2).run(suite)


class TestReadFilterClass(unittest.TestCase):

    def test_str(self):
        date = datatypes.Datatype(
            'Date',
            {
                'year': '2013'
            }
        )
        filter = commands.Read.Filter(
            'older-than',
            'date',
            date
        )
        self.assertEqual(
            str(filter),
            '<Filter type=older-than field=date>'
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestReadFilterClass)
unittest.TextTestRunner(verbosity=2).run(suite)
