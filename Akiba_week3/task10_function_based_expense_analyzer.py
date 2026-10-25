expenses=[]
def add_an_expense(description,category,amount):
  expense={}
  expense["description"]=description
  expense["category"]=category
  expense['amount']=amount
  expenses.append(expense)
  return expenses
def calculate_total_expenses(expenses):
  total=0
  for item in expenses:
    total +=item["amount"]
  return total
def calculate_spending_by_category(expenses,category):
  total=0
  for item in expenses:
    if item["category"]==category:
      total +=item["amount"]
  return total
def find_the_largest_expense(expenses):
    largest1=expenses[0]["amount"]
    largest2=expenses[0]['description']
    for item in expenses:
      if item["amount"]>largest1:
        largest1= item["amount"]
        largest2=item["description"]

    return (f" the largest expenses is {largest2}--{largest1}")
def identify_expenses_above_threshold(expenses,threshold):
  above=[]
  for item in expenses:
    if item["amount"]>threshold:
       above.append(item)
  return above
def generate_spending_report(expenses):
  total=calculate_total_expenses(expenses)
  category1=calculate_spending_by_category(expenses,category)
  largest=find_the_largest_expense(expenses)
  above=identify_expenses_above_threshold(expenses,200)


  print ("======Spending Report========")
  print(f"Total expense {total}")
  print(f"Spending by category \n {category1}")
  print(f"Largest expenses \n {largest}")
  print(f"Expenses above200 \n {above}")
   

def calculate_category_percentages(expenses):
    total = calculate_total_expenses(expenses)
    category_totals = {}

    for item in expenses:
        category = item["category"]
        amount = item["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    percentages = {}

    for category, amount in category_totals.items():
        if total > 0:
            percentages[category] = (amount / total) * 100
        else:
            percentages[category] = 0

    return percentages

def find_highest_spending_category(expenses):
    category_totals = {}

    for item in expenses:
        category = item["category"]
        amount = item["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    if not category_totals:
        return None

    highest_category = ""
    highest_total = 0

    for category in category_totals:
        if category_totals[category] > highest_total:
            highest_total = category_totals[category]
            highest_category = category

    return highest_category, highest_total

expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]

print("Total expenses:", calculate_total_expenses(expenses))

print("Food spending:",
      calculate_spending_by_category(expenses, "Food"))

print("Largest expense:", find_the_largest_expense(expenses))

print("Expenses above 200:",
      identify_expenses_above_threshold(expenses, 200))

print("Category percentages:",
      calculate_category_percentages(expenses))

print("Highest spending category:",
      find_highest_spending_category(expenses))
