#Monopoly.py
import random

class Player:
    def __init__(self): #once constructor is implemented then Original Object def won't work
        self.position = 1
        #Taking a Turn in Monopoly
    def turn(self):
         #("It's your turn.")
        doubles = 3
        # doubles = 3, roll the dice, if equal then check if it's their last life, if not, take a life and roll again, if not double end go
        while doubles > 0:
            die_1 = random.randint(1,6)
            die_2 = random.randint(1,6)
            sum_of_dice = die_1 + die_2
            if die_1 == die_2:
                self.position = self.position + sum_of_dice
                if doubles == 1:
                    #print("You Are In Jail")
                    self.position = 10
                doubles -= 1
            else:
                self.position = self.position + sum_of_dice
                break
               
        #after the 39th tile, the player returns to go
        if self.position > 39:
            self.position = self.position - 39
            #print("You passed GO again!!")
        #print("Final Position: ", self.position)
        return self.position




dec = list()
maz = list()
declan = Player()
#print("Take your first turn. You are on Go or position: ", declan.position)

for x in range(100):
    dec.append(declan.turn())
    maz.append(declan.turn())

print(dec)
print(maz)

