# some fibonacci fun

## first generate a Fibonacci sequence less than or equal to four million
## next sum the even-valued terms
import time

def evenFibonacci(limit):
    num1 = 1
    num2 = 2
    fibonnaci_list = list()
    fibonnaci_list.append(num2)
    numsum = num1 + num2
    while numsum < limit:
        numsum = num1 + num2
        if numsum > limit:
            break
        if numsum%2 == 0:
            fibonnaci_list.append(numsum)
        num1 = num2
        num2 = numsum
    return sum(fibonnaci_list)

print(evenFibonacci(4000000))
print(time.process_time())
    

