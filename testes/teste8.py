"""Exercise: Odd or Even
Write a program that works out whether if a given number is an odd or even 
number. (e.g. take input from a user)."""

#  Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
    print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder).
else:
    print("This is an odd number.")
