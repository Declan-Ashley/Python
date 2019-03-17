#list comprehensions

a = [1,3,5,7,9,11]
# [2,6,10,14,18,22]

c = []
for x in a:
    c.append(x * 2)
print(c)

#List Comprehension
d = [x * 2 for x in a] # This executes the same as the for loop above
print(d)


#[1, 4, 9, 16, 25, 36]

e1 = []
for x in range(1, 7):
    e1.append(x ** 2)
print(e1)


#List Comprehension
e2 = [x ** 2 for x in range(1,7)]
print(e2)
# [36, 25, 16, 9, 4, 1]

e3 = []
for x in range(6, 0, -1):
    e3.append(x ** 2)
print(e3)

#List Comprehension
e4 = [x ** 2 for x in range(6,0, -1)]
print(e4)
