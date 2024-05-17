def get_revenue_or_expenses():
    
    user_response = True
    income_and_expenses_data = {}
    
    while user_response:
    
        transaction_name = input("Enter transaction name: ")
        amount = input("Enter amount (use negative sign for expense): ")
        
        
        if transaction_name.upper() in income_and_expenses_data:
            if amount[0] == "-":
                income_and_expenses_data[transaction_name.upper()] -= int(amount[1:])
            else:
                income_and_expenses_data[transaction_name.upper()] += int(amount)
        else:
            income_and_expenses_data[transaction_name.upper()] = int(amount)
            
            
        another = input("Another? (Y/N): ")
            
            
        if another.upper() == "N":
            user_response = False
    
    return income_and_expenses_data

get_revenue_or_expenses()