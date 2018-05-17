# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import base

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestBaseClass(unittest.TestCase):

    def test_str(self):
        self.assertEqual(
            str(base._Base()),
            '<_Base>'
        )

    def test_main(self):
        self.assertFalse(
            base._Base()._main()
        )

    def test_tostring(self):
        self.assertEqual(
            base._Base().tostring(),
            b''
        )

    def test_tostring_header(self):
        b = base._Base()
        b._header = True
        self.assertEqual(
            b.tostring(),
            b'<?xml version="1.0" encoding="utf-8"?>'
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestBaseClass)
unittest.TextTestRunner(verbosity=2).run(suite)
