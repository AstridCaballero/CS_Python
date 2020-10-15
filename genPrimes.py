def genPrimes():
    n = 2       
    while True:
        prime = True
        for num in range(2, n):
            if n % num == 0: 
                prime = False               
                break              
        if prime:
            yield n
        n += 1

myP = genPrime()
print(myP)
print(myP.__next__())
print(myP.__next__())