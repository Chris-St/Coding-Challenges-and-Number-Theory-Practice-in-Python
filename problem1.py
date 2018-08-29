# natural number fun

def sumNatural(limit):
    numlist = list()
    for num in range(1,limit):
        if num % 3 == 0:
            numlist.append(num)
        elif num % 5 == 0:
            numlist.append(num)
    return sum(numlist)
        
   
print(sumNatural(1000))
    
