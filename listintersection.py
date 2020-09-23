"""****************************
List intersection of two lists
****************************"""

#create the lists
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

#for the shortcut
list_c = []

#initialize variables
count = 0
a = 0
b = 0

#create intersection (loop)
while a < 5:
	while b < 5:
		if  ( list_a[a] == list_b[b]):
			list_c.append(list_a[a])
		b = b + 1

	b = 0
	a = a + 1

#output
print("THe Intersection is: ")
for value in list_c:
	print(value, end = " ")