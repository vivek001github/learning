# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the portion of salary to be saved (as a decimal): "))
# total_cost = float(input("Enter the cost of your dream home: "))

# portion_down_payment = 0.25  
# current_savings = 0
# r = 0.04 

# monthly_salary = annual_salary / 12
# down_payment = total_cost * portion_down_payment

# months = 0

# while current_savings < down_payment:
#     current_savings += current_savings * (r / 12) 
#     current_savings += monthly_salary * portion_saved  
#     months += 1

# print("Number of months:", months)





# annual_salary = 80000
# portion_saved = 0.1
# total_cost = 800000

# portion_down_payment = 0.25 * total_cost
# current_savings = 0
# r = 0.04
# months = 0
# semi_annual_raise = 0.03

# while current_savings < portion_down_payment:
    
#     # current_savings += current_savings * r / 12 + annual_salary / 12 * portion_saved
#     portion_salary_saved = annual_salary / 12 * portion_saved
#     monthly_portion_saved = current_savings * r / 12
#     current_savings += monthly_portion_saved + portion_salary_saved

#     months += 1
#     if months % 6 == 0:
#         annual_salary += annual_salary*semi_annual_raise
    
# print("Number of months:", months)






# annual_salary = 150000
# total_cost = 1000000
# portion_down_payment = 0.25 * total_cost
# r = 0.04
# semi_annual_raise = 0.07
# months = 36  

# low = 0
# high = 1
# epsilon = 0.01
# steps = 0

# while True:
#     portion_saved = (low + high) / 2
#     current_savings = 0
#     updated_salary = annual_salary

#     for month in range(months):
#         portion_salary_saved = updated_salary / 12 * portion_saved
#         monthly_portion_saved = current_savings * r / 12
#         current_savings += monthly_portion_saved + portion_salary_saved

#         if month % 6 == 5:
#             updated_salary += updated_salary * semi_annual_raise

#     if abs(current_savings - portion_down_payment) < epsilon:
#         break
#     elif current_savings < portion_down_payment:
#         low = portion_saved
#     else:
#         high = portion_saved

# print("Best savings rate:", round(portion_saved, 4))
# print("steps in bisection search:",steps)


starting_salary = 150000
total_cost = 1000000
down_payment = 0.25 * total_cost
semi_annual_raise = 0.07
annual_return = 0.04
monthly_return = annual_return / 12
months = 36

low = 0
high = 1
epsilon = 0.01
steps = 0

while True:
    steps += 1
    portion_saved = (low + high) / 2 
    current_savings, updated_salary = 0, starting_salary

    for month in range(months):
        current_savings += updated_salary / 12 * portion_saved + current_savings * monthly_return
        if month % 6 == 5:
            updated_salary += updated_salary * semi_annual_raise

    if abs(current_savings - down_payment) < epsilon:
        break
    elif current_savings < down_payment:
        low = portion_saved 
    else:
        high = portion_saved 

print("Best savings rate:", round(portion_saved, 4))
print("Steps in bisection search:", steps)

