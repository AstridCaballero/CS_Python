def ccBalance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    balance: input positive number int or float. The outstanding balance on the credit card
    annualInterestRate: input positive float. Annual interest rate
    monthlyPaymentRate: input positive float. Monthly payment rate

    returns: credit card balance after one year if a person only pays 
    the minimum monthly payment required by the credit card company each month.
    '''
    for i in range(12):
        # Calculate monthly payment
        min_month_pay = monthlyPaymentRate * balance        
        # Calculate monthly balance after payment
        balance = balance - min_month_pay        
        # Calculate monthly interest rate 
        month_interest_r = annualInterestRate / 12.0
        # calculate updated balance each month. Balance after monthly interest rate is applied
        balance = round((balance + (balance * month_interest_r)), 2)
           
    print("Remaining balance: " + str(balance))
    return balance

y = ccBalance(42, 0.2, 0.04)