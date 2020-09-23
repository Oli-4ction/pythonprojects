"""**************************

Binary to Decimal converter 

**************************""" 

#function

def binToDec():  

    #Initialize the variables 

    decimal = 0 

    z_answer = 0 

    binary = int(input("Please enter your binary number: ")) 

    #the loop 

    while(binary!= 0): 

        dec = binary % 10 

        decimal = decimal + (dec * (2 ** z_answer)) 

        binary = binary // 10 

        z_answer += 1 

    #calling the function  

    print("The decimal number is:", decimal) 

  
#output
binToDec() 
