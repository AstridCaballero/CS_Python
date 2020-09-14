def ccBalance(balance, annualInterestRate):
    '''
    balance: input positive number int or float. The outstanding balance on the credit card
    annualInterestRate: input positive float. Annual interest rate    

    returns: The lowest monthly payment that will pay off all debt in under 1 year. 
    The monthly payment must be a multiple of $10.
    '''
    count = 0
    epsilon = 0    
    # Calculate a guess of fixed monthly payment
    min_fix_month_pay = (balance + (balance * annualInterestRate)) // 12    
    # Fixed monthly payment must be a multiple of $10
    if (min_fix_month_pay % 10) < 5:
        min_fix_month_pay = round(min_fix_month_pay - (min_fix_month_pay % 10))
    else:
        min_fix_month_pay = round(min_fix_month_pay + (10 - (min_fix_month_pay % 10)))
    
    # Calculate monthly interest rate 
    month_interest_r = annualInterestRate / 12.0
    balance_temp = -1
    while count < 11:        
        min_fix_month_pay = min_fix_month_pay - epsilon 
        print(min_fix_month_pay)
        balance_temp = balance   
        for i in range(12):                        
            # Calculate monthly balance after payment
            balance_temp = balance_temp - min_fix_month_pay
            print(balance_temp)
            # Check if full payment is achieved before 12 months
            if balance_temp < 0:                 
                epsilon = 10 
                count = 0         
                break 
            # calculate updated balance each month. Balance after monthly interest rate is applied
            balance_temp = round((balance_temp + (balance_temp * month_interest_r)), 2)
            count += 1   
    # Calculate final fixed monthly payment. if balance_temp is positive, 
    # code has gone one step too far so fixed monthly payment is one epsilon samller
    # thus we need to add epsilon (10) to the last guess.
    if balance_temp > 0:
        min_fix_month_pay = min_fix_month_pay + epsilon  
    print("Lowest Payment: " + str(min_fix_month_pay))
    return min_fix_month_pay

y = ccBalance(417, 0.2)