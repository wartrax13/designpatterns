"""
TemplateMethod is a behavior pattern.
It's uses subclass for customizer and to define 
the objects without change the skeleton class. 
When many algoritms get a logic similar, this pattern is very useful.
"""

from abc import ABCMeta, abstractmethod

class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

class iOSCompiler(Compiler):
    def collectSource(self):
        print('Collecting Swift Source Code')
    
    def compileToObject(self):
        print('Compiling Swift code to LLVM bitcode')
    
    def run(self):
        print('Program runing on runtime environment')

iOS = iOSCompiler()
iOS.compileAndRun()