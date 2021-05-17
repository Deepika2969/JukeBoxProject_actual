
greeting = 'Hello'
name = 'Deepika'


#This i susing FORMAT method.

#place holders 
message = '{}, {}. Welcome!'.format(greeting,name)
print(message)

#Instance 3:
print ('This is a {}'.format('STRING'))

#Instance 2:
print ('{},{},{}'.format('fox','Cat','Dog'))
print ('{2},{1},{0}'.format('fox','Cat','Dog'))

# f Strings
message = f'{greeting}, {name}. Welcome!'
print(message)

#best part of f strings is we can code in the flower braces

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

# indentation using formatting

print('{0:5} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:10}'.format('Apples', 3.))

print('{0:<10}'.format('left'))
print('{0:>10}'.format('Right'))
print('{0:^10}'.format('Centre'))

# Precision of floating numbers
## Using format method
result = 100/77
print(result)

print('The result is {}'.format(result))
print('The precised result is {r:1.2f}'.format(r=result))

##Using f strings
print(f'The precised result is {result:1.5}')



