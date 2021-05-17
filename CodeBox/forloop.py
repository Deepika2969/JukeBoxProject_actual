my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
	print(num)

for num in my_list:

	if (num % 2 == 0):
		print(f'{num} is even')
	else:
		print(f'{num} is odd')

for num in my_list:
	print("Hello")

for _ in my_list:
	print(_)

	sum = 0
for num in my_list:
	sum = sum + num

print(sum)

name = "Deepika"
for letter in name:
	print("Hellllo!!!!!!!!")
	for letter in name:
		print(letter)

my_tuple = (1,2,3,'Dp')
for item in my_tuple:
	print(item)

my_tuplist = [(1,2),(3,4),(5,6)]
for item in my_tuplist:
	print(item)

#Unpacking of Tuples:

for item1,item2 in my_tuplist:
	print(f'{item1} and {item2}')
	print(item1)
	print(item2)

my_Dictionary = {'name':'Dp','age':45,'Sex':'FM'}
for detail in my_Dictionary:
	print(detail)
for keys in my_Dictionary.keys():
    print (keys)
for values in my_Dictionary.values():
	print(values)
for key,value in my_Dictionary.items():
	print (f'{key}:{value}')