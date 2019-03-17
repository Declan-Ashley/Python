#No10.py

# Initialize a list
primes = []
for possiblePrime in range(2, 2000000):

    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1): #check for composite numbers
        if possiblePrime % num == 0:
            isPrime = False
            break #makes loop more effiecient

    if isPrime:
        primes.append(possiblePrime)


print(sum(primes))
