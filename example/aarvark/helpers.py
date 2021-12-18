from unittest import TestCase
from dataclasses import dataclass


try:
    print()
except (ValueError, TypeError) as err:
    pass


try:
    print()
except ValueError or IndexError:
    pass


async def qux():
    pass

async def quux():
    qux()


value = 'a'


isinstance(value, str) or isinstance(value, int)


class Bar:
    @classmethod
    def cm():
        pass


value is 1

value != True


@dataclass
class Bar:
    pass


class Bar(TestCase):
    def foo(self):
        self.assertEquals("a", "b")

    def bar(self):
        self.assertTrue("a", "b")
