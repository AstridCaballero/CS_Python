def ccBalance(balance, annualInterestRate):
    '''
    balance: input positive number int or float. The outstanding balance on the credit card
    annualInterestRate: input positive float. Annual interest rate    

    returns: The lowest monthly payment that will pay off all debt in under 1 year. 
    The monthly payment must be a multiple of $10.
    '''
    m_interest_rate = (annualInterestRate) / 12.0   
    m_pay_lower_bound = balance / 12
    m_pay_upper_bound = (balance * pow((1 + m_interest_rate),12)) / 12.0  
    m_middle = round(((m_pay_lower_bound + m_pay_upper_bound) / 2), 2)

    # while loop to perform bisection search. Our guess is the middle value
    while m_pay_lower_bound <= m_pay_upper_bound:
        balance_temp = balance
        #  Apply guess (m_middle) to the montlhy payments for a year
        for i in range(12):
            # Calculate monthly balance after payment
            balance_temp = balance_temp - m_middle
            # check if balance is negative, which means debt has been payed in full
            if balance_temp < 0:
                break   
            # calculate updated balance each month. Balance after monthly interest rate is applied if 
            # balance is positive (meaning there is still debt)
            balance_temp = balance_temp + (balance_temp * m_interest_rate)            
            

        # Check if full payment is achieved before 12 months
        # meaning m_middle was too high
        if balance_temp < 0 and i < 12:                 
            m_pay_upper_bound = m_middle - 0.01
            m_middle = round(((m_pay_lower_bound + m_pay_upper_bound) / 2), 2) 
            
        # m_middle was too low
        elif balance_temp > 0:
            m_pay_lower_bound = m_middle + 0.01
            m_middle = round(((m_pay_lower_bound + m_pay_upper_bound) / 2), 2)
           
           
        else:
            break
   
    print(m_middle)

y = ccBalance(238591, 0.18)