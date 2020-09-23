"""*************************
Decimal to binary converter
*************************"""
#function
def function():
    #intialize variables
    number = 0
    intermediateResult = 0
    remainder = []

    number = int(input("Enter your decimal number: "))
    base = int(input("Choose the number format: "))
    #loops
    while number != 0:
            remainder.append(number % base)
            number = number // base
            remainder.reverse()
    for result in remainder:
       print(result, end = "")
#output
function()


