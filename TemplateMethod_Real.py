"""
In this case, we can use a real example.
Imagine that we have a transporte agency that offer two types of trips.
Both offer 3 days of travel with different experiences.
As both have 3 days, we can use the same class structure.
We define the AbstractClass for uncouple and define the object away.
The TravelAgency is a Client or the TemplateMethod,
which will run the plan depending on the choice. 
"""

from abc import abstractmethod, ABCMeta

class Trip(metaclass=ABCMeta):

    @abstractmethod
    def setTransport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def returnHome(self):
        pass

    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()


class VeniceTrip(Trip):
    def setTransport(self):
        print('Take a boat and find your way in the Grand Canal')
    
    def day1(self):
        print('Visit St Marks Basilica in St Marks Square')
    
    def day2(self):
        print('Appreciate Doges Palace')
    
    def day3(self):
        print('Enjoy the food near the Rialto Bridge')
    
    def returnHome(self):
        print('Get souvenirs for friends and get back')


class MaldivesTrip(Trip):
    def setTransport(self):
        print('On foot, on any island, Wow!')
    
    def day1(self):
        print('Enjoy the marine life of Banana Reef')
    
    def day2(self):
        print('Go for the water sports and snorkellig')
    
    def day3(self):
        print('Relax on the beach and enjoy the sun')
    
    def returnHome(self):
        print('Dont feel like like leaving the beach...')


class TravelAgency:
    def arrange_trip(self):
        choice = input('What kind of place you do like to go historical or to a beach?')
        if choice == 'historical':
            self.trip = VeniceTrip()
            self.trip.itinerary()
        if choice == 'beach':
            self.trip = MaldivesTrip()
            self.trip.itinerary()

TravelAgency().arrange_trip()