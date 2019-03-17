#bmiCalculater.py

name = "Declan Ashley:"
#in m
height = 2

#in kg
weight = 90

#function for BMI
def BMI(height, weight):
    bmi = weight / (height ** 2)
    if bmi < 25:
        print(name + " is not Overweight")
    elif bmi == 25:
        print(name + " is at risk of becoming Overweight")
    else:
        print(name + " is Overweight")

BMI(height, weight)
