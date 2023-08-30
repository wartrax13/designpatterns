"""Factory is a creation pattern (or a concept).
There are two types of factory: simple Factory and Factory Method.
Client, Factory, create_type, Abstract, Product1, Product2.

"""
from abc import abstractmethod, ABCMeta


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print('Au au au!!')
    
class Cat(Animal):
    def do_say(self):
        print('Miau Miau')

class Ave(Animal):
    def do_say(self):
        print('aaaaaaaaaa') 

# Forest Factory defined
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()
    
# Client Code
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input('Whice animal should make_sound, Dog or Cat?')
    ff.make_sound(animal)