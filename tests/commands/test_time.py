# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestTimeClass(unittest.TestCase):

    def test_str(self):
        self.assertEqual(
            str(commands.Time()),
            '<Time>'
        )

    def test_time(self):
        self.assertIsInstance(
            commands.Time().time(),
            ET.Element
        )

    def test_tostring(self):
        self.assertEqual(
            commands.Time().tostring(),
            b'<Time />'
        )

    def test_prettify(self):
        self.assertEqual(
            commands.Time().prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<Time/>\n'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestTimeClass)
unittest.TextTestRunner(verbosity=2).run(suite)
