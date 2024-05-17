def gross_pay(wage, work_duration):
    """function to calculate gross pay of user

    Args:
        wage (float): Hourly pay rate
        work_duration (float): duration of work

    Returns:
        float: gross pay
    """
    return float(work_duration) * float(wage)

def federal_tax(gross_pay, percentage=10):
    """function to calculate federal tax for username

    Args:
        gross_pay (int): gross pay of user
        percentage (int, optional): deduction percentage. Defaults to 10.

    Returns:
        float: Deducted tax amount
    """
    return (percentage/100) * gross_pay

def state_tax(gross_pay, percentage=5):
    """Function to calculate state tax for users

    Args:
        gross_pay (int): gross pay of user
        percentage (int, optional): deduction percentage. Defaults to 5.

    Returns:
        float: Deducted tax amount
    """
    return (percentage/100) * gross_pay

def social_security(gross_pay, percentage=6.2):
    """function to calculate social security

    Args:
        gross_pay (float): gross pay of user
        percentage (float, optional): deduction percentage. Defaults to 6.2.

    Returns:
        float: deducted tax amount
    """
    return (percentage/100) * gross_pay

def net_pay():
    """function to calculate net pay for users

    Returns:
        string: string representing gross pay, federal tax, state tax, social security, and net pay
    """
    
    wage = input("What is your hourly wage? ")
    work_duration = input("How many hours did you work? ")
    
    grossPay = gross_pay(wage, work_duration)
    
    federalTax = federal_tax(grossPay)
    stateTax = state_tax(grossPay)
    socialSecurityTax = social_security(grossPay)
    
    withholding_sum = withholding(federalTax, stateTax, socialSecurityTax)
    
    net_pay = grossPay - withholding_sum
    
    return "Gross Pay: $%0.2f(%0.1f hours @ $%0.2f/hr)\nFederal tax: $%0.2f\nState tax: $%0.2f\nSocial security: $%0.2f\nNet pay: $%0.2f" % (grossPay, float(work_duration), float(wage), federalTax, stateTax, socialSecurityTax, net_pay)

def withholding(federalTax, stateTax, socialSecurityTax):
    """function to calculate withholding elements sum

    Args:
        federalTax (float): federal tax amount
        stateTax (float): state tax amount
        socialSecurityTax (float): social security tax amount

    Returns:
        float: total sum of withholding elements
    """
    return sum([federalTax, stateTax, socialSecurityTax])

def show_discretionary_income(dict_of_revenue_and_expenses):
    """function to show discretionary income for users

    Args:
        dict_of_revenue_and_expenses (dict): dictionary of revenue and expenses

    Returns:
        string: string values for revenue, expenses and discretionary values
    """
    
    revenue = sum([v for v in dict_of_revenue_and_expenses.values() if v > 0]) 
    expenses = sum([v for v in dict_of_revenue_and_expenses.values() if v < 0]) 
    
    return "Revenue: $%0.2f Expenses: $%0.2f Discretionary: $%0.2f" % (revenue, expenses, revenue + expenses)

def get_revenue_or_expenses():
    """function to get the revenue and expenses of users

    Returns:
        dictionary: dictionary of revenue and expenses
    """
    
    user_response = True
    income_and_expenses_data = {}
    
    while user_response:
    
        transaction_name = input("Enter transaction name: ")
        amount = input("Enter amount (use negative sign for expense): ")
        print() # print a blank line
        
        if transaction_name.upper() in income_and_expenses_data:
            if amount[0] == "-":
                income_and_expenses_data[transaction_name.upper()] -= float(amount[1:])
            else:
                income_and_expenses_data[transaction_name.upper()] += float(amount)
        else:
            income_and_expenses_data[transaction_name.upper()] = float(amount)
            
            
        another = input("Another? (Y/N): ")
            
            
        if another.upper() == "N":
            user_response = False
    
    return income_and_expenses_data


def show_menu():
    """function to show the menu

    Returns:
        string: string representation of the user's choice between 1 & 4
    """
    choice = input("1-Calculate net pay\n2-Enter revenue or expense\n3-Show discretionary income\n4-Exit\nChoice ")
    print() # print a blank line
    return choice

def main():
    """main entry point for the applicaton
    """
    state = True
    
    get_revenue_or_expenses_data = ""
    
    while state:
        choice = show_menu()
        if choice == "1":
            print(net_pay())
            print() # print a blank line        
        elif choice == "2":
            get_revenue_or_expenses_data = get_revenue_or_expenses()
        elif choice == "3":
            print(show_discretionary_income(get_revenue_or_expenses_data))
            print() # print a blank line
        elif choice == "4":
            state = False
            print("Thanks for using My Finance!")
        else:
            print("Please enter a valid choice betwee 1 and 4!")
        
if __name__ == "__main__":
    main()