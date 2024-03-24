# If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("Welcome to the tip calculator.\nWhat was the total bill? "))

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

amount_of_people = input("How many people to split the bill? ")

total = int(bill) * (1 + int(percentage) / 100)

each = round(total / int(amount_of_people), 2)

each = "{:.2f}".format(each)

print(f"Each person should pay: ${each}")