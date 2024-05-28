"""Exercise: Days in a Month
Write a program that works out the number of days in a month."""

age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
years_left = 90 - int(age)
weeks_left = years_left * 52
print(f"You have {weeks_left} weeks left.")
