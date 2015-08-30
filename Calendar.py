#Classes: Parent, Event, Current
#time passes too (1sec), 1sec = 1min

#PARENT CLASS
#   define the time (__init__)

#EVENT CLASS
#   define notification system
#   def past or future

#CURRENT CLASS
#   not sure

#AUTO UPDATE FUNCTION
#   get current time (year, day)
#   for loop
#       1 sec wait
#       check if any digits are at max before adding 1 sec on

#NOTIFICATION FUNCTION
#   if current equals any event class print notification
#   change status from future to past

#EVENT CREATION FUNCTION
#    ask for name
#    create
#    ask for description   

class Parent(object):
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

class Event(Parent):
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def getNotification(self, note):
        self.note = note
        
    def PrintNotification(self):
        print(self.note)
        
class Current(Parent):
    def __init__(self, year, month, day, hour, minute, second):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        
def AutoUpdate():
    pass

def CreateEvent():
    pass

def EventNotification():
    pass    