"""The rollercoaster has two types of tickets: Adult and Child."""

# Diferenciando if, elif e else.
# Se o valor for maior que 120, o valor vai para o if.
# Se for menor que 120, o valor vai para o else.

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
