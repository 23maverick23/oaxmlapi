# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestAddClass(unittest.TestCase):

    def test_str(self):
        project = datatypes.Datatype(
            'Project',
            {'name': 'New project'}
        )
        self.assertEqual(
            str(commands.Add('Project', {}, project)),
            '<Add type=Project>'
        )

    def test_add(self):
        project = datatypes.Datatype(
            'Project',
            {'name': 'New project'}
        )
        self.assertIsInstance(
            commands.Add('Project', {}, project).add(),
            ET.Element
        )

    def test_tostring(self):
        project = datatypes.Datatype(
            'Project',
            {'name': 'New project'}
        )
        self.assertEqual(
            commands.Add('Project', {}, project).tostring(),
            (
                b'<Add type="Project"><Project><name>New project</name>'
                b'</Project></Add>'
            )
        )

    def test_tostring_enable_custom(self):
        project = datatypes.Datatype(
            'Project',
            {'name': 'New project'}
        )
        self.assertEqual(
            commands.Add('Project', {'enable_custom': '1'}, project).tostring(),
            (
                b'<Add enable_custom="1" type="Project"><Project><name>'
                b'New project</name></Project></Add>'
            )
        )

    def test_prettify(self):
        project = datatypes.Datatype(
            'Project',
            {'name': 'New project'}
        )
        self.assertEqual(
            commands.Add('Project', {}, project).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<Add type="Project">\n'
                b'  <Project>\n'
                b'    <name>New project</name>\n'
                b'  </Project>\n'
                b'</Add>\n'
            )
        )

    def test_invalid_type_user(self):
        with self.assertRaises(Exception):
            user = datatypes.Datatype(
                'User',
                {'name': 'John Doe'}
            )
            commands.Add('User', {}, user)

    def test_invalid_type_company(self):
        with self.assertRaises(Exception):
            company = datatypes.Datatype(
                'Company',
                {'company': 'John Doe Inc.'}
            )
            commands.Add('Company', {}, company)

suite = unittest.TestLoader().loadTestsFromTestCase(TestAddClass)
unittest.TextTestRunner(verbosity=2).run(suite)
