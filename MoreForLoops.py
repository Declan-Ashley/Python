#Examples - More For loops

a = ['apple', 'banana', 'republic']

for e in a:
    print(e)

for i in range(0, 3): #0, 1 and 2 - does not include 3. Could also use range(len(a))
    for j in range(i + 1):
        #Prints apple once, banana twice, republic thrice
        print(a[i])
