import six
import unittest
from scrapy.utils import trackref
from tests import mock


class Foo(trackref.object_ref):
    pass


class Bar(trackref.object_ref):
    pass


class TrackrefTestCase(unittest.TestCase):

    def setUp(self):
        trackref.live_refs.clear()

    def test_format_live_refs(self):
        o1 = Foo()  # NOQA
        o2 = Bar()  # NOQA
        o3 = Foo()  # NOQA
        self.assertEqual(
            trackref.format_live_refs(),
            '''\
Live References

Bar                                 1   oldest: 0s ago
Foo                                 2   oldest: 0s ago
''')

        self.assertEqual(
            trackref.format_live_refs(ignore=Foo),
            '''\
Live References

Bar                                 1   oldest: 0s ago
''')

    @mock.patch('sys.stdout', new_callable=six.StringIO)
    def test_print_live_refs_empty(self, stdout):
        trackref.print_live_refs()
        self.assertEqual(stdout.getvalue(), 'Live References\n\n\n')

    @mock.patch('sys.stdout', new_callable=six.StringIO)
    def test_print_live_refs_with_objects(self, stdout):
        o1 = Foo()  # NOQA
        trackref.print_live_refs()
        self.assertEqual(stdout.getvalue(), '''\
Live References

Foo                                 1   oldest: 0s ago\n\n''')

    def test_get_oldest(self):
        o1 = Foo()  # NOQA
        o2 = Bar()  # NOQA
        o3 = Foo()  # NOQA
        self.assertIs(trackref.get_oldest('Foo'), o1)
        self.assertIs(trackref.get_oldest('Bar'), o2)
        self.assertIsNone(trackref.get_oldest('XXX'))

    def test_iter_all(self):
        o1 = Foo()  # NOQA
        o2 = Bar()  # NOQA
        o3 = Foo()  # NOQA
        self.assertEqual(
            set(trackref.iter_all('Foo')),
            {o1, o3},
        )
