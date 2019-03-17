# File: example.py
print ("Hello World!")

#Function example
def personalDetails(Name, LastName, DOB, CurrentDate):
    age = CurrentDate - DOB
    fullName = Name + " " + LastName
    return fullName, age

#init multiple variables from personalDetails(): name = fullName; age = age
name, age = personalDetails("Declan", "Ashley", 1995, 2019)

#Print to console
print("My name is " + name + " and I am ", age, " old! I just wrote a python function")

#exponents - to the power of
sq = 2 ** 2
cube = 2 ** 3

#PlusEquals allows you to add to a variable
sq += cube

#Turn an int to a string
str(sq)


a, b = 3, 2

#If Statement
if a < b:
    print("a is definetely less than b")
print("Not sure")


#If Else
c,d = 3,4
if c < d:
    print("c is less than d")
else:
    print("c is not less than d")

#Else if condition:
    pass
e,f = 4,4
if e < f:
    print("e is less than f")
elif e == f:
    print("e is the same as f")
else:print("e is not less than f")

#Nested If Else
g, h = 9, 8

if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is the same as h")
    else:
        print("g is not less than h")

#Functions
def convert(miles):
    km = miles * 1.6
    return km

print(convert(15))



#Lists
list = [3, 10, -1]
#Adds 1 to the list
list.append(1)

list.append("Hello")
list.append([150, -5])

#remove last value from list
list.pop()

#list.pop(0) removes the first item from the list
print(list)


#input() Function
message = input("Tell me spomething, and I will repeat it: ")
print(message)

#presonlising a message
prompt = "Hello, my name is Declan."
prompt += "\nWhat's your name? "

name = input(prompt)
print("\nHello " + name + "! It's a real pleasure to meet you")

#convert string to an int using - int()
question = ("How old are you? ")
age = input(question)
age = int(age)
if age >= 18:
    print("let's go get a drink")
else:
    print("Where's your babysitter kid?")

#These exercises are taken from the book - Python Crash Course
#7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”
greeting = "Hey there, how can I help? Looking for a particular car today? "
response = input(greeting)
print("Let me see if I can find you a " + response + " today!!")

#7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.
greeting_2 = "How many people are in your dinner group? "
response_2 = input(greeting_2)
response_2 = int(response_2)
if response_2 > 8:
    print("I am very sorry. You may have to wait for a table. Please follow me to the bar")
else:
    print("After me. You have the finest table in the house.")

#7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.
trick = "Give me any number and I will tell you if it is a multiple of 10."
rep = input(trick)
rep = int(rep)
if rep % 10 == 0:
    print(rep, " is a multiple of 10")
else:
    print(rep, " is not a multiple of 10")

#7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.

print("Any toppings for your pizza? To stop say when!! ")
res = ""
flag = True
while flag:
    res = input()
    if res == "when":
        flag = False
        print("Okay Bye")
        break
    print("\nSure, anything else?")



#7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are
#between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost
#of their movie ticket.

ticket_greet = "Hello - what's your age? "

while True:
    holder_age = input(ticket_greet)
    if holder_age == "quit":
        break
    else:
        holder_age = int(holder_age)
    if holder_age < 3:
        print('The ticket is free')
    elif holder_age < 12:
        print('The ticket is $10')
    else:
        print('The ticket is $15')
