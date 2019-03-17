#ProjectEuler.net No.4

pal = 0
pal_list = []
y = 100
for x in range(100, 1000):
    for y in range(100, 1000):
        pal = x * y
        if str(pal) == str(pal)[::-1]:
                pal_list.append(pal) #Adds pal to the list

#Made poor mistake - sorted(pal_list) THIS IS NOT HOW TO USE SORT ON LIST!!
pal_list.sort()
for a in pal_list:
    print(a)
