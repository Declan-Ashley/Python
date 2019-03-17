#No 7

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

# Initialize a list
primes = []
for possiblePrime in range(2, 1000000):

    # Assume number is prime until shown it is not.
    isPrime = True
    for num in range(2, int(possiblePrime ** 0.5) + 1): #check for composite numbers
        if possiblePrime % num == 0:
            isPrime = False
            break #makes loop more effiecient

    if isPrime:
        primes.append(possiblePrime)

if len(primes) > 10001:
    print(primes[10000])
