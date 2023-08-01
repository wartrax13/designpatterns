"""
Singleton is a pattern of criation.
The object don't is created in memory but is repeated.
"""
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print('Object created', s)

s1 = Singleton()
print('Object created', s1)
