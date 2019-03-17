#Sets in python

a = set()
#add to a set
a.add(1)
a.add(2)

print(a)

#iteration
for x in a:
    print(x)

#When to use a set - Remove duplicates
given_list1 = [1,2,3,4,2]

new_set = set()
for x in given_list1:
    new_set.add(x)
print(new_set)

# Create new list with only unique elements from the Original list
new_list = [] # or list()
for x in new_set:
    new_list.append(x)
print(new_list)


c = set()
c.add('apple')
c.add('banana')
c.add(1)
print(c)

#Exercise - Sum of Unique Numbers
given_list2 = [1,3,4,1,3]
set = set()
temp = 0

for x in given_list2:
    set.add(x)
for y in set:
    temp += y

print(temp)
