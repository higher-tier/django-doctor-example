from unittest import TestCase


class TestBar(TestCase):
    def test_foo(self):
        self.assertEquals("a", "b")

    def test_bar(self):
        self.assertTrue("a", "b")
