print('hello world')

if 5 > 2:
    print('You are correct!')

x = 5
y = 'hello world`'

#this is a comment
print( x )

x = str( 3 )
y = int( 3 )
z = float( 3 )

print(type( x ))
print(type( y ))

x, y, z = 'Orange', 'Banana', 'Cherry'
print(x, y, z )

#! OR

x = y = z = 'Orange'
print( x, y, z )

fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print( x, y, z )

num1 = 5
num2 = 9

print( num1 + num2 )

msg = 'Great Work!'
def myFunc():
    print(msg)

myFunc()


test = 'awesome'

def func():
    global test 
    test = 'fantastic'

func()
print('Python is ' + test)