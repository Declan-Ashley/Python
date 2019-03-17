#largest_prime_factor.py

#Largest Prime Factor of 600851475143

value = 600851475143
set = set()


#My solution - This doesn't have a prime number checker
#for x in range(1, 10000000):
#    if value % x == 0:
#        set.add(x)
#        set.add(value / x)

#s = sorted(set)
#print(s)

#Solution found after answer was correctly found - much cleaner and simply produces reult
result = []
y = 600851475143
for x in range(2, 600851475143):
    if x > y:
        break
    for i in range(0, x):
        if y%x == 0: # Checks X is a factor
            y = int(y/x) #Divide and Update the Current Y value by the X value you know is a factor
            result.append(x)
print(max(result))
