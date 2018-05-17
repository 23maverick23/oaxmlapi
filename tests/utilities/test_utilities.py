# -*- coding: utf-8
from __future__ import absolute_import, print_function
import unittest
from oaxmlapi import utilities

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestUtilitiesClass(unittest.TestCase):

    def test_json_str_true(self):
        xml_res = (
            '<response><Auth status="0"/><Read status="0">'
            '<Invoice><total> 99.00 </total></Invoice></Read></response>'
        )
        self.assertEqual(
            utilities.xml2json(xml_res, strip=True),
            (
            '{"response": {"Auth": {"@status": "0"}, "Read": {'
            '"@status": "0", "Invoice": {"total": "99.00"}}}}'
            )
        )

    def test_json_str_false(self):
        xml_res = (
            '<response><Auth status="0"/><Read status="0">'
            '<Invoice><total> 99.00 </total></Invoice></Read></response>'
        )
        self.assertEqual(
            utilities.xml2json(xml_res, strip=False),
            (
            '{"response": {"Auth": {"@status": "0"}, "Read": {'
            '"@status": "0", "Invoice": {"total": " 99.00 "}}}}'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestUtilitiesClass)
unittest.TextTestRunner(verbosity=2).run(suite)
