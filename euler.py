#euler.py

#P.1 - Multiples of 3 & 5
tmp = 0
for x in range (1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        tmp += x
#print(tmp)

#P.2 - Even Fib numbers

## Example 2: Using recursion
def fibR(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    return fibR(n-1)+fibR(n-2)

#Original way I solved it !!

# Sum of all Even Fib numbers that are < 4,000,000
sum = 0
#for x in range(1, 33): #33rd Fib Sequence is 4000000+
#    if fibR(x) % 2 == 0:
#        sum += fibR(x)
#print(sum)

#Found in answers - Uses lists and is much faster/cleaner
l=[1,2]
while l[-1]<=4e6: l.append(l[-1]+l[-2])
print(sum(x for x in l[:-1] if x%2 ==0))
