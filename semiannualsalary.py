# Homework 2
# Justin Cheung
# Created April 20th, 2026
# Last Modified: April 21st, 2026

# Created in purpose to calculate the number of months need to 
# Get a down payment for a house with various salaries and portioned savings

PORTION_DOWN_PAYMENT = 0.25
RATE = 0.04

annual_salary = int(input("What's your annual salary? \n"))
portion_saved = float(input("\nWhat percentage as a decimal do you save? \n"))
total_cost = int(input("\nWhat's the cost of your dream home? \n"))
semi_annual_raise = float(input("\nWhat's your semi-annual raise as a decimal\n"))

current_savings = 0
months = 0
amount_needed = PORTION_DOWN_PAYMENT * total_cost

while current_savings < amount_needed:
    
    monthly_interest = current_savings * (RATE/12)

    if months % 6 == 0 and months != 0:
        annual_salary *= (1 + semi_annual_raise)

    monthly_deposit = (annual_salary / 12) * portion_saved
    
    current_savings += monthly_interest + monthly_deposit
    
    months += 1
    
percentage = PORTION_DOWN_PAYMENT * 100

print(f"\nIt will take: {months} months to save for a \n{percentage}% down payment on that home")
    

