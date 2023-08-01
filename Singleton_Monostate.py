"""
Example Singleton monostate.
"""

class Borg:
    __shared_state = {'1': '2'}
    def __init__(self) -> None:
        self.x = 1
        self.__dict__ = self.__shared_state
        pass

b = Borg()
b1 = Borg()
b.x = 4

print('Borg object "b": ', b)
print('Borg object "b1"', b1)
print('Object state "b"', b.__dict__)
print('Object state "b1"', b1.__dict__)

# Here we can do the same thing with method __new__
class Borg2(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(Borg2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj

b = Borg2()
b1 = Borg2()
b.x = 4

print('Borg object "b": ', b)
print('Borg object "b1"', b1)
print('Object state "b"', b.__dict__)
print('Object state "b1"', b1.__dict__)