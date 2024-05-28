"""Exercise: Body Mass Index 2.0
Write a program that calculates and prints the Body Mass Index (BMI) from a
user's weight and height."""

# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
IMC = int(weight) / float(height) ** 2

if IMC < 18.5:
    print("Your BMI is " + str(IMC) + ", you are underweight.")
elif IMC < 25:
    print("Your BMI is " + str(IMC) + ", you have a normal weight.")
elif IMC < 30:
    print("Your BMI is " + str(IMC) + ", you are slightly overweight.")
elif IMC < 35:
    print("Your BMI is " + str(IMC) + ", you are obese.")
else:
    print("Your BMI is " + str(IMC) + ", you are clinically obese.")
