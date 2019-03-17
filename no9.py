#No9.py


# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a ** 2 + b ** 2 = c ** 2

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.

#create a list
list = list()
#Nested loop working up to 1000
for b in range(1, 1000):
    for a in range(1, b):
        if (a ** 2) + (b ** 2) == (1000 - (a + b)) ** 2:
            list.append(a) #store values in a list
            list.append(b)

c = 1000 - (list[0] + list[1]) #Find the C value
list.append(c)#Add to list

print(list[0] * list[1] * list[2])
