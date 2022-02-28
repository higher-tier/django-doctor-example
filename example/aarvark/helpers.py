from dataclasses import dataclass


try:
    print()
except (ValueError, TypeError) as err:
    pass


try:
    print()
except ValueError or TypeError:
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


value = 1,

value = {1, 'b', 'c' 'd', 1}

        
with Foo as bar:
    with open('some/path.json', 'r') as file:
        content = json.loads(file.read())

        
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated'
    )
}
