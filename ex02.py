#while loops and break statements
total = 0
i = 1
while i < 5:
    total += i
    i += 1
print(total)


given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total_2 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total_2 += given_list[i]
    i += 1
print(total_2)

#How a break works
given_list = [5, 4, 4, 3, 1, -2, -3, -5]
total_3 = 0
i = 0
for e in given_list:
#checks here if e goes below 0 - it breaks if it does
    if e <= 0:
        break
#sum while e is above 0
    total_3 += e
print(total_3)

total_4 = 0
#j is index
j = 0
while True:
    total_4 += given_list[j]
    j +=  1
    if given_list[j] <= 0:
        break
print(total_4)

#problem - find the sum of all negative numbers - Right Value
given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
z = 0
total_5 = 0
#while loop
while j < len(given_list3):
#if j is less than 0 add given_list3[j]
    if given_list3[j] < 0:
        total_5 += given_list3[j]
#increment j
    j += 1
print(total_5)


#tutorial solution - This allows for starting the loop from 0 and working back negatively as we know the list descends in order(given in the exercise description)
#given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
#total_5 = 0
#j = len(given_list3) - 1
#while given_list3[j] < 0:
#    total_5 += given_list3[j]
#    j -= 1
#print(total_5)
