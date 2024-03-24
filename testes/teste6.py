# 1st input: enter height in meters e.g: 1.65
height = input("Quanto é sua altura em m? ")
# 🚨 Don't change the code above 👆
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Quanto é seu peso em kg? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

IMC = int(weight) / float(height) ** 2
IMC2 = str(int(IMC))
print("Seu índice de Massa Corporal" + " " + IMC2)