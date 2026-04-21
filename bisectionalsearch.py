# Homework 2
# Justin Cheung
# Created April 20th, 2026

semi_annual_rate = 0.07
rate = 0.04
down_payment_rate = 0.25
total_cost = 1000000

down_payment = down_payment_rate * total_cost


months = 0
current_savings = 0

low = 0
high = 10000
num_guesses = 0



annual_salary = int(input("Please enter your annual salary: \n"))

while abs(high - low) > 1:
    
    num_guesses += 1
    guess_rate = (high + low) / 2

    current_savings = 0
    months = 0
    temp_annual_salary = annual_salary

    for months in range(1, 37):
        
        monthly_deposit = (temp_annual_salary/12) * (guess_rate/10000)
        
        if months % 6 == 0:
            temp_annual_salary *= 1 + semi_annual_rate

        current_savings *= 1 + (rate/12)

        current_savings = current_savings + monthly_deposit


    if current_savings < down_payment:
        if abs(current_savings - down_payment) <= 100:
           break 
        low = round(guess_rate, 5)

    else:
        if abs(current_savings - down_payment) <= 100:
            break
        high = round(guess_rate, 5)
print("\nResults:\n")

if high == 10000:
    print("Not possible :(")
else:
    print(f"Best savings rate| {round(guess_rate/10000, 4)}")
    print(f"Steps in bisection search| {num_guesses}")
