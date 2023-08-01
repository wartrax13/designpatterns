"""
Metaclass is a class entry another class.
"""
### Example of metaclass
class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print('*** Here is my int ***', args)
        print('Now do whatever you want with these objets...')
        return type.__call__(cls, *args, **kwargs)

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4, 5)

#### Now the metaclass will be a Singleton

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                MetaSingleton, cls
            ).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
    pass

logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)