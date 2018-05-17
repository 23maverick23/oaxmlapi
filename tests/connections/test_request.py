# -*- coding: utf-8
from __future__ import absolute_import
import unittest
from oaxmlapi import connections, datatypes, commands

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class TestRequestClass(unittest.TestCase):

    def test_str(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        auth = connections.Auth('company', 'username', 'p@ssw0rd')
        time = [commands.Time().time()]
        self.assertEqual(
            str(connections.Request(app, auth, time)),
            '<Request client=test company=company username=username>'
        )

    def test_request(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        auth = connections.Auth('company', 'username', 'p@ssw0rd')
        time = [commands.Time().time()]
        self.assertIsInstance(
            connections.Request(app, auth, time).request(),
            ET.Element
        )

    def test_tostring_auth(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        auth = connections.Auth('company', 'username', 'p@ssw0rd')
        time = [commands.Time().time()]
        self.assertEqual(
            connections.Request(app, auth, time).tostring(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>'
                b'<request API_ver="1.0" client="test" client_ver="1.0" '
                b'key="abc123" namespace="default"><Auth><Login>'
                b'<company>company</company><user>username</user>'
                b'<password>p@ssw0rd</password></Login></Auth>'
                b'<Time /></request>'
            )
        )

    def test_tostring_remoteauth(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        remoteauth = connections.RemoteAuth('company', 'username', 'p@ssw0rd')
        time = [commands.Time().time()]
        self.assertEqual(
            connections.Request(app, remoteauth, time).tostring(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>'
                b'<request API_ver="1.0" client="test" client_ver="1.0" '
                b'key="abc123" namespace="default"><RemoteAuth><Login>'
                b'<company>company</company><user>username</user>'
                b'<password>p@ssw0rd</password></Login></RemoteAuth>'
                b'<Time /></request>'
            )
        )

    def test_tostring_noauth(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        user = datatypes.Datatype('User', {'id': '1234'})
        time = [commands.Time().time()]
        with self.assertRaises(Exception):
            connections.Request(app, user, time).request()

    def test_tostring_nodata(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        auth = connections.Auth('company', 'username', 'p@ssw0rd')
        self.assertEqual(
            connections.Request(app, auth, None).tostring(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>'
                b'<request API_ver="1.0" client="test" client_ver="1.0" '
                b'key="abc123" namespace="default"><Auth><Login>'
                b'<company>company</company><user>username</user>'
                b'<password>p@ssw0rd</password></Login></Auth></request>'
            )
        )

    def test_prettify(self):
        app = connections.Application('test', '1.0', 'default', 'abc123')
        auth = connections.Auth('company', 'username', 'p@ssw0rd')
        time = [commands.Time().time()]
        self.assertEqual(
            connections.Request(app, auth, time).prettify(),
            (
                b'<?xml version="1.0" encoding="utf-8"?>\n'
                b'<request API_ver="1.0" client="test" client_ver="1.0" key="abc123" namespace="default">\n'
                b'  <Auth>\n'
                b'    <Login>\n'
                b'      <company>company</company>\n'
                b'      <user>username</user>\n'
                b'      <password>p@ssw0rd</password>\n'
                b'    </Login>\n'
                b'  </Auth>\n'
                b'  <Time/>\n'
                b'</request>\n'
            )
        )

suite = unittest.TestLoader().loadTestsFromTestCase(TestRequestClass)
unittest.TextTestRunner(verbosity=2).run(suite)
