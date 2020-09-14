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
    m_middle = round(((m_pay_lower_bound + m_pay_upper_bound) / 2), 0)
   
    if (m_middle % 10) < 5:
        m_middle = round(m_middle - (m_middle % 10))
    else:
        m_middle = round(m_middle + (10 - (m_middle % 10)))
    # print(m_middle)
    
    
    while m_pay_lower_bound <= m_pay_upper_bound:
        balance_temp = balance
        for i in range(12):
            # Calculate monthly balance after payment
            balance_temp = balance_temp - m_middle    
            if balance_temp < 0:
                break   
            # calculate updated balance each month. Balance after monthly interest rate is applied
            balance_temp = balance_temp + (balance_temp * m_interest_rate)
            # print(balance_temp)
            

        # Check if full payment is achieved before 12 months
        # meaning m_middle was too high
        if balance_temp < 0 and i < 11:                 
            m_pay_upper_bound = m_middle - 10
            m_middle = round(((m_pay_lower_bound + m_pay_upper_bound) / 2), 0)  
            if (m_middle % 10) < 5:
                m_middle = round(m_middle - (m_middle % 10))
            else:
                m_middle = round(m_middle + (10 - (m_middle % 10)))          
                  
            
        # m_middle was too low
        elif balance_temp > 0: # and (balance_temp - m_middle > 0)
            m_pay_lower_bound = m_middle + 10
            m_middle = round(((m_pay_lower_bound + m_pay_upper_bound) / 2), 0)
            if (m_middle % 10) < 5:
                m_middle = round(m_middle - (m_middle % 10))
            else:
                m_middle = round(m_middle + (10 - (m_middle % 10)))
           
        else:
            break

    # if i == 11 means that the full payment was completed on the 12th month
    # if i < 11 means full payment was completed before 12 months but lower bound became > than upper bound
    # so the whilw loop gets broken and as middle has been updated using the new lower_bound
    # we need to get the previous middle value by adding 10
    if i < 11:
        m_middle = m_middle + 10
    print(m_middle)

y = ccBalance(417, 0.2)