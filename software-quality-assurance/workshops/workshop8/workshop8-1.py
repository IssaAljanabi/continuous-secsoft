from ast import operator
import random

def divide(v1, v2):
    temp = 0
    if (isinstance(v1, int)) and (isinstance(v1, int)):
        if v2 > 0:
            temp = v1/ v2
        elif v2 < 0:
            temp = v1/ v2
        else:
            print("Divisor is zero. provide non-zero value")
    else:
            temp = "Invalid input. Please provide numeric values."
    return temp
def fuzzyValues():
    # positive /expected software testing
    #res = divide(2, 1)
    # Negative software testing: divisor check > 0 values
    #res = divide(2, -1)
    # Negative software testing: divisor check < 0 values
    #res = divide(2, 0)
    #Negative software testing: check types: exmaple 1
    res = divide (2, '1')
    #Negative software testing: check types: exmaple 2
    res = divide ('2', '1')
    
    print(res)
    print('='*100)
    
def simpleFuzzer():
    fuzzyValues()


if __name__=='__main__':
    simpleFuzzer()

