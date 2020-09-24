"""************************
Simple Maximum Selction
************************"""
#Import Function randrange() from Modul random
from random import randrange

#the max number of values
max_nr = 10

#eine leere Liste für die Werte
values = []

print("Simple Maximum Selction")

#fill the list with random numbers until 200
pass_through = 1
while pass_through <= number:
    values.append(randrange(1, 1000))
    pass_through = pass_through + 1

#xcheck output
print("THe unsorted values are: ")
for value in values:
    print(value, end = " ")

#as long as there is more than one element in the unsorted section
k = number - 1
while k > 0:
    #the last element will be the provisional maximum
    maximum = k
    #go through the unsorted section
    i = 0
    while i < k:
        #is the current element the new maximum?
        if values[maximum] < values[i]:
            maximum = i
        i = i + 1

    #swop the values
    if maximum != k:
        swop_temp = values[k]
        values[k] = values[maximum]
        values[maximum] = swap_temp
    k = k - 1

#the sorted output
print()
print("The sorted values are: ")
for value in values:
    print(value, end = " ")
