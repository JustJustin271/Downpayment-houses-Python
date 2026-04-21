# Homework 2
# Justin Cheung
# Created April 20th, 2026
# Last Modified: April 21st, 2026

# Created in purpose to caculathe number
# Of months needed to save for a downpayment

current_savings = 0
portion_down_payment = 0.25
rate = 0.04
months = 0

annual_salary = int(input("What's your annual salary? \n\n"))
portion_saved = float(input("\nWhat percentage as a decimal do you save? \n\n"))
total_cost = int(input("\nWhat's the cost of your dream home? \n\n"))

amount_needed = portion_down_payment * total_cost

while current_savings < amount_needed:
    
    monthly_interest = current_savings * (rate/12)
    
    monthly_deposit = (annual_salary / 12) * portion_saved
    
    current_savings += monthly_interest + monthly_deposit
    
    months += 1
    
percentage = portion_down_payment * 100

print(f"\nIt will take: {months} months to save for a \n{percentage}% down payment on that home")
    

