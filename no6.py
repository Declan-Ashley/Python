#ProjectEuler.net no6.py


sum = 0
sq = 0
for x in range(1, 101):
    sum = x + sum
    sq = (x ** 2) + sq

sum = sum ** 2
print(sum, sq)
print(sum - sq)
