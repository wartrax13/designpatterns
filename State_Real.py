"""

"""

class ComputerState(object):
    name = 'state'
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print('Current:', self, ' => switched to new state', state.name)
            self.__class__ = state
        else:
            print('Current:', self, ' => switching to', state.name, 'not possible.')
    
    def __str__(self) -> str:
        return self.name


class Off(ComputerState):
    name = 'off'
    allowed = ['on']


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()
    
    def change(self, state):
        self.state.switch(state)
    

if __name__ == '__main__':
    comp = Computer()
    # Liga
    comp.change(On)
    # Desliga 
    comp.change(Off)

    # Liga novamente
    comp.change(On)
    # Suspende
    comp.change(Suspend)
    # Try hibernate
    comp.change(Hibernate)
    # Liga novamente
    comp.change(On)
    # Desliga
    comp.change(Off)