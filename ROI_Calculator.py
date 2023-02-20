# create an empty list to store the expenses, total investment
expenses = []
total_investment = []
# Defines the amount of income the user's property generates per month
income = input("Enter the income per month of the property.")
# ask the user to input expenses until they enter 'done'
while True:
    expense = input("Enter a monthly expense or type 'done' to finish: ")
    if expense == 'done':
        break
    expenses.append(expense)
total = 0
# Adds income to total
total = total + int(income)
# Subtracts the total monthly expenses from the monthly income
for num in range(0, len(expenses)):
    total = total - int(expenses[num])
# prints the cash flow 
print("Total monthly cash flow:",total,"Dollars")
# Asks user to enter initial investment to be used in the final calculations
total_investment = input("Enter your initital investment amounts or type 'done' to finish: ")
      
yearly_cashflow = (total * 12)
# Divides yearly_cashflow and the users total investment creating a decimal number   
ROI = yearly_cashflow / int(total_investment)
# Converts decimal to percentage by multiplying then adds comments and '%' using the fstring
final_result = ROI * 100
print(f'Return on Investment per year:{final_result:.2f}%')
