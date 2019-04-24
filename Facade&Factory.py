# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 17:00:02 2019

@author: ttc
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:36:12 2019

@author: ttc
"""

#%%
# a simple factory implementation
class Factory():
    def __init__(self, type):
        self.type = type

    @staticmethod
    def __new__(self,type):
        try:
            MyObj = eval(type)()
        except NameError:
            print('Name Error Exception')
            return(None)
        
        if isinstance(MyObj, object):
            return MyObj
        else:
            raise Exception ('Unsupported Type')     

# a simple facade implementation           
class EventManager(object):
    Services = ['Hotelier','Florist','Caterer','Musician']
    
    def __init__(self):
        print("Event Manager:: Let me talk to the folks\n")
    def arrange(self):
        for service in self.Services:
            Factory(service).provideService()

class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? --")
    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True
    def provideService(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")
            
class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? --")
    def provideService(self):
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")

class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event --")
    def provideService(self):
        print("Chinese & Continental Cuisine to be served\n\n")
        
class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage --")
    def provideService(self):
        print("Jazz and Classical will be played\n\n")
        
class You(object):
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!!")
    def askEventManager(self):
        print("You:: Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()
    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Phew!")


#%%

if __name__ == "__main__":
    you = You()
    you.askEventManager()