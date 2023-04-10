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
    # Negative software testing: divisor check < 0 small float values
    #res = divide(2, 0.0001)
    # Negative software testing: divisor check > large float values
    #res = divide(2, 999999.7771)    
    #Negative software testing: check types: exmaple 1
    #res = divide (2, '1')
    #Negative software testing: check types: exmaple 2
    #res = divide ('2', '1')
    #Negative software testing: check types: exmaple 3 'NULL'
    #res = divide (2, 'NULL')
    #Negative software testing: check types: exmaple 4 'NaN'
    #res = divide (2, 'NaN')
    #Negative software testing: check types: exmaple 5 '‘-1E+02’as '
    #res = divide (2, '-1E+02’as')
    #Negative software testing: check types: exmaple 6 '‘0xffffffffffffffff’as '
    #res = divide (2, '0xffffffffffffffff')
    #Negative software testing: check types: exmaple 7 '-9223372036854775808/-1'
    #res = divide (2, '-9223372036854775808/-1')
    #Negative software testing: check types: exmaple 8 '<>?:\"{}|_+/-1'
    #res = divide (2, '<>?:\"{}|_+/-1')
    #Negative software testing: check types: exmaple 9 '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999'
    res = divide (2, '999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999')   
    
    print(res)
    print('='*100)
    
def simpleFuzzer():
    fuzzyValues()


if __name__=='__main__':
    simpleFuzzer()

