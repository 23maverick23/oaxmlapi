# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import commands, datatypes

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestCreateUserClass(unittest.TestCase):

    def test_str(self):
        company = datatypes.Datatype(
            'Company',
            {'nickname': 'Acme Inc'}
        )
        user = datatypes.Datatype(
            'User',
            {'nickname': 'admin', 'password': 'p@ssw0rd', 'email': 'admin@acme.com'}
        )
        self.assertEqual(
            str(commands.CreateUser(company, user)),
            '<CreateUser nickname=admin>'
        )

    def test_create(self):
        company = datatypes.Datatype(
            'Company',
            {'nickname': 'Acme Inc'}
        )
        user = datatypes.Datatype(
            'User',
            {'nickname': 'admin', 'password': 'p@ssw0rd', 'email': 'admin@acme.com'}
        )
        self.assertIsInstance(
            commands.CreateUser(company, user).create(),
            ET.Element
        )

    def test_tostring(self):
        company = datatypes.Datatype(
            'Company',
            {'nickname': 'Acme Inc'}
        )
        user = datatypes.Datatype(
            'User',
            {'nickname': 'admin', 'password': 'p@ssw0rd', 'email': 'admin@acme.com'}
        )
        self.assertEqual(
            commands.CreateUser(company, user).tostring(),
            (
                b'<CreateUser><Company><nickname>Acme Inc</nickname></Company>'
                b'<User><nickname>admin</nickname><password>p@ssw0rd</password>'
                b'<addr><Address><email>admin@acme.com</email></Address></addr>'
                b'</User></CreateUser>'
            )
        )

    def test_prettify(self):
        company = datatypes.Datatype(
            'Company',
            {'nickname': 'Acme Inc'}
        )
        user = datatypes.Datatype(
            'User',
            {'nickname': 'admin', 'password': 'p@ssw0rd', 'email': 'admin@acme.com'}
        )
        self.assertEqual(
            commands.CreateUser(company, user).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<CreateUser>\n'
                b'  <Company>\n'
                b'    <nickname>Acme Inc</nickname>\n'
                b'  </Company>\n'
                b'  <User>\n'
                b'    <nickname>admin</nickname>\n'
                b'    <password>p@ssw0rd</password>\n'
                b'    <addr>\n'
                b'      <Address>\n'
                b'        <email>admin@acme.com</email>\n'
                b'      </Address>\n'
                b'    </addr>\n'
                b'  </User>\n'
                b'</CreateUser>\n'
            )
        )

    def test_invalid_company_nickname(self):
        company = datatypes.Datatype(
            'Company',
            {}
        )
        user = datatypes.Datatype(
            'User',
            {'nickname': 'admin', 'password': 'p@ssw0rd', 'email': 'admin@acme.com'}
        )
        with self.assertRaises(Exception):
            commands.CreateUser(company, user).create()

    def test_invalid_user_nickname(self):
        company = datatypes.Datatype(
            'Company',
            {'nickname': 'Acme Inc'}
        )
        user = datatypes.Datatype(
            'User',
            {'password': 'p@ssw0rd', 'email': 'admin@acme.com'}
        )
        with self.assertRaises(Exception):
            commands.CreateUser(company, user).create()

    def test_invalid_user_email(self):
        company = datatypes.Datatype(
            'Company',
            {'nickname': 'Acme Inc'}
        )
        user = datatypes.Datatype(
            'User',
            {'nickname': 'admin', 'password': 'p@ssw0rd'}
        )
        with self.assertRaises(Exception):
            commands.CreateUser(company, user).create()

    def test_invalid_user_password(self):
        company = datatypes.Datatype(
            'Company',
            {'nickname': 'Acme Inc'}
        )
        user = datatypes.Datatype(
            'User',
            {'nickname': 'admin', 'email': 'admin@acme.com'}
        )
        with self.assertRaises(Exception):
            commands.CreateUser(company, user).create()

suite = unittest.TestLoader().loadTestsFromTestCase(TestCreateUserClass)
unittest.TextTestRunner(verbosity=2).run(suite)
