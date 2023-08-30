"""
Facotory Method is a creation pattern.

The eval method is responsable for many thing with math.
In this case, it's used for to get the class with the name. 
The classes is create thought of the Abstract Method.
So the code stay uncople, 
for the next modifications, creating new objects generically.
The creation code is separate from code that uses it.
"""
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass


class PersonalSection(Section):
    def describe(self):
        print('Profile section.')


class AlbumSection(Section):
    def describe(self):
        print('Album section.')


class PatentSection(Section):
    def describe(self):
        print('Patente section.')
    

class PublicationSection(Section):
    def describe(self):
        print('Publication Section.')


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.createProfile()
    
    @abstractmethod
    def createProfile(self):
        pass

    def getSections(self):
        return self.sections

    def addSections(self, section):
        self.sections.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__ == '__main__':
    profile_type = 'linkedin' # can be facebook
    profile = eval(profile_type.lower())()
    print('Creating Profile', type(profile).__name__)
