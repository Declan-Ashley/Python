#classes.py

class Robot:
    #constructor
    def __init__(self, givenName, givenColour, givenWeight): #once constructor is implemented then Original Object def won't work
        self.name = givenName
        self.colour = givenColour
        self.weight = givenWeight
    def introduce_self(self):
        print("My name is " + self.name) #this in java

#Robot Object
#r1 = Robot()
#r1.name = "Tom"
#r1.colour = "red"
#r1.weight = 30

#r2 = Robot()
#r2.name = "Jerry"
#r2.colour = "blue"
#r2.weight = 40

#best practice for attributes is using a constructor
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)



r1.introduce_self()
r2.introduce_self()
print(r1.colour)

#New Class - Person
class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
    def sit_down(self):
        self.isSitting = True

    def standUp(self):
        self.isSitting = False


p1 = Person("Alice", "Aggressive", False)
p2 = Person("Becky", "talkative", True)


#New attribute given - Robot Owned
p1.robot_owned = r2
p2.robot_owned = r1

#This calls the introduce_self() function inside robot1
p1.robot_owned.introduce_self()
