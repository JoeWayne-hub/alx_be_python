#Ask user for their monthly income 

monthly_income = float(input("Enter your monthly income:"))

#Ask user for their monthly expenses

monthly_expenses = float(input("Enter your total monthly expenses: "))

#Calculate monthly savings 
monthly_savings = monthly_income - monthly_expenses

#Project savings over a year with interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)


#Print results 

print(f"Your monthly savings are ${monthly_savings}. ")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
