"""
As I was explaining, when we need to do the same operation, 
it is recommended to use a AbstractClass with abstractmethods 
just define the logic, because it will be the same aways.
In this example, the pattern becomes clearer.
Here we have AbstractClass, a ConcreteClass and a Client (template_method) or a executor. 
"""

from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def template_method(self):
        print('Defining the Algorithm. Operation1 follows Operation2')
        self.operation2()
        self.operation1()

class ConcreteClass(AbstractClass):

    def operation1(self):
        print('My Concrete Operation1')
    
    def operation2(self):
        print('Operation 2 remains same')

class Client:
    def main(self):
        self.concreate = ConcreteClass()
        self.concreate.template_method()

client = Client()
client.main()