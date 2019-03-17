#ex01.py - Exercise CS Dojo: Switching List orders

list = ["banana", "apple", "microsoft"]
print(list)

#Here we switch the list order by using a temp variable
temp = list[0]
list[0] = list[2]
list[2] = temp

print(list)

#Shortcut - does the same as above
list[0], list[2] = list[2], list[0]
print(list)

#Prints all elements
for element in list:
    print(element)

#Sum of all elements in list b
b = [5, 10, 25, 100]
total = 0
#Element can be replaced by any value
for e in b:
    total = total + e
print(total)

#Sum of a range
total_2 = 0
#range function range(1, 5) gives 1,2,3,4
for i in range(1, 5):
    total_2 += i
print(total_2)

total_3 = 0

for i in range(1, 8):
    if i % 3 == 0:
        total_3 += i
print(total_3)


#sum of all multiples of 3 and 5 that are less than 100
total_4 = 0


#May not be correct value
for i in range(1, 100):
    #checks if i is multiple of 3 && 5 - if it is then add them
    if i % 3 == 0 or i % 5 == 0:
        total_4 += i
print(total_4)
