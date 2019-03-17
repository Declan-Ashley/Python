#ProjectEuler.net No.5
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
list = list()
num = 2520

while len(list) == 0:
    if num % 20 == 0 and num % 19 == 0 and num % 18 == 0 and num % 17 == 0 and num % 16 == 0 and num % 15 == 0 and num % 14 == 0 and num % 13 == 0 and num % 12 == 0 and num % 11 == 0:
        list.append(num)
    else:
        num += 1

print(num)


#factors of 10 = 5,2,1,10
#factors of 9 = 9, 3, 6, 2, 1
#Factors of 8 = 8, 4, 2, 1
#factors of 7 = 7, 1
# f20 = 20, 10, 5, 4, 2, 1
#f19 = 19, 1
#f18 = 18, 9, 2, 1
#f17 = 17, 1
#f16 = 16, 8, 4, 2, 1
#15 = 3, 5
#14 = 14, 7, 2, 1
#13
#12 = 12, 6, 4, 3, 2
#11
