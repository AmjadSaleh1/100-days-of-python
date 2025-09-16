#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator\n")
Bill = float(input("What was the total bill?"))
Tip = int(input("How much tip would you like to give?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = Tip/100*Bill + Bill

EachPersonPay = bill_with_tip/people
#Pillperperson = round(EachPersonPay, 2)
Pillperperson = "{:.2f}".format(EachPersonPay)
print(f"Each Person should pay : {Pillperperson}$")

