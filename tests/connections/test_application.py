# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import connections


class TestApplicationClass(unittest.TestCase):

    def test_str(self):
        self.assertEqual(
            str(connections.Application('test', '1.0', 'default', 'abc123')),
            '<Application client=test version=1.0>'
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestApplicationClass)
unittest.TextTestRunner(verbosity=2).run(suite)
