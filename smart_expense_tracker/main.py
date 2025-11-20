import json
import os
from datetime import datetime
import time

def load_expenses(filename="expenses.json"):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except (FileNotFoundError):
        print("File you are looking for is not Found.")
        return []


def save_expenses(data, filename="expenses.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


#Decorator to Calculate the Execution time of a particular Function it is applied on.
def log_and_time(func):
    def wrapper(*args, **kwargs):

        start_time = time.time()
        start_dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time

        log_entry = f"{start_dt} | Function '{func.__name__}' executed in {duration:.6f}seconds."

        print(f"{log_entry.strip()}")
        print("-"*30)
        with open("app_log.txt", "a") as log_file:
            log_file.write(log_entry+"\n")
        return result
    return wrapper

@log_and_time
def add_expense():

    expenses = load_expenses()

    #1.Date
    date_input = input("Enter date in (YYYY-MM-DD) Format or press \"Enter\" for today: ").strip()
    if date_input == "":
        date_input = datetime.today().strftime("%Y-%m-%d") 
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")
            return
        
    #2.Category
    category = input("Enter category (e.g., Food, Travel, Shopping, Bills): ").strip()
    if category == "":
        print("Category cannot be empty.")
        return
    
    #3.Amount
    try:
        amount = float(input("Enter amount: ").strip())
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    
    #4.Description
    user_input = input("Do You want to add Description: (Yes/No)?").strip().lower()
    if(user_input=="yes"):
        description = input("Enter description: ").strip()
    else:
        description = "---"

    new_expense = {
        "date": date_input,
        "category": category,
        "amount": amount,
        "description": description
    }

    expenses.append(new_expense)
    save_expenses(expenses)
    print("Expense added successfully!")
    print("-"*30)

@log_and_time
def view_expenses():

    expenses = load_expenses()  

    if not expenses:
        print("No expenses found! Add Expenses.")
        return
    
    expenses.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))

    total = 0
    for exp in expenses:
        date = exp["date"]
        category = exp["category"]
        amount = exp["amount"]

        if exp["description"]:
            description = exp["description"] 
        else:
            "---"

        total += amount
        print(f"Date: {date:12} |Category:  {category:12} | Amount: {amount:10.2f} | Description: {description}")

    print("-" * 60)
    print(f"Total Monthly Expense: ₹{total:.2f}")
    print("-"*30)

@log_and_time
def generate_monthly_summary():

    expenses = load_expenses()

    if not expenses:
        print("No expenses found! Add some expenses.")
        return

    try:
        month_input = int(input("Enter month (1-12): ").strip())
        year_input = int(input("Enter year: ").strip())
        if not (1 <= month_input <= 12):
            print("Invalid month! Month Must be 1-12.")
            return
    except ValueError:
        print("Invalid input! Enter numeric month and year.")
        return

    monthly_expenses = []

    for exp in expenses:
        date_obj = datetime.strptime(exp["date"], "%Y-%m-%d")
        if date_obj.month == month_input and date_obj.year == year_input:
            monthly_expenses.append(exp)

    if not monthly_expenses:
        print(f"No expenses found for {month_input}/{year_input}.")
        return
    
    if(len(monthly_expenses)>1):
        monthly_expenses.sort(key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d"))
    
    summary = {}
    total_amount = 0
    for exp in monthly_expenses:
        category = exp["category"]
        amount = exp["amount"]
        total_amount += amount
        summary[category] = summary.get(category, 0) + amount

    for category, amount in summary.items():
        print(f"Category: {category} |  Amount: {amount:.2f}")
    print("-" * 30)
    print(f"Overall Total: ₹{total_amount:.2f}")


#Saving this Report Option:

    save_choice = input("Do you want to save this summary as JSON? (y/n): ").strip().lower()
    if save_choice == "y":
        filename = f"summary_{year_input}_{month_input:02d}.json"
        with open(filename, "w") as file:
            json.dump({
                "month": month_input,
                "year": year_input,
                "summary": summary,
                "total": total_amount
            }, file, indent=4)
        print(f"Summary saved as {filename}")
        print("-"*30)


def main():
    while True:
        print("===== Smart Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Generate Monthly Summary")
        print("4. Exit")
        print("--------------------------------")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_monthly_summary()
        elif choice == "4":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
