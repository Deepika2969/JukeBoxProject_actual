#works with Key value pair.Dictionary can hold any mutable data type.(Sp no tuples because they are Immutable)

student = {'name':'Deepika', 'age':45,'course':['Maths','Biology','History']}
print(student['name'])
print(student['age'])
print(student['course'])
print(student)
#print(student['phone'])  # Will get a Key error 
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone','Key Not Found'))
#print(student.get('name','Key Found')) It will just return the name aadn doenot go to the second parameter

#how to add a new entry to the dictionary

student_1 = {'name':'Deepika', 'age':45}
print(student_1)
student_1.update({'course':['Maths','Biology','History']})
print(student_1)
student_1.update({'course':['Maths','Biology','History'],'age':50})
print(student_1)

#How to delete a key from Dictionary
del student_1['age']
print(student_1)

N=student_1.pop('name')
print(student_1)
print(N)

#to count the number of keys and values and to List them.

print(len(student))
print(student.keys())
print(student_1.values())
print(student.items())

#iterate through the dictionary

example = {'name':'Dp','age':25,'Sex':'FM'}
for key,values in example.items():
	print(key,values)