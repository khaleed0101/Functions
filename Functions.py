#using functions

def add_one (x):
    return x + 1

a = add_one(5)

print(a)

if a == 6:
    print('you guessed the number')
else:
    print('you did not guess the number')

#how is the valuable?
b = add_one(7)
c = add_one(9)
d = add_one(12)

#parametre
# a faction can have one parameter, no parameters, or many parameters

#no parameters

def add_two():
    return 2 + 2
result = add_two()
print(result)

#multiple parameters
def add_nums(x, y, z):
    return x + y + z
total = add_nums(2, 7, 3)
print(total)

total2 = add_nums(total, 5, 6)
print(total2)

#Reusing functions
#PRINT A PROGRAM THAT DETERMINE IF NUMBERS IS EVEN OR ODD
X = int(input('Enter number...'))
if X % 2 == 0:
    print('it is old')
else:
    print('it is odd')

n =int(input('Enter number'))
if n % 2 == 0:
    print('n is even')
else:
    print('n is odd')

#with a function

def even_odd():
    n = int(input('Enter number '))

    if n % 2 == 0:
        print('n and is even')
    else:
        print('n is odd')
    
    for i in range (5):
        even_odd

x = True
while x == True:
    print('''Menu
          
    1) Add two numbers
    2) Multiply two numbers''')
    user = int(input('Enter selections'))
    if user == 1:
        first_num = int(input('Enter a number'))
        second_num = int(input('Enter a number'))
        print(first_num + second_num)
    elif user == 2:
        first_num = int(input('Enter a number: '))
        second_num = int(input('Enter a number: '))
        print(first_num *  second_num)
    else:
        x = False
        print('Invalid number')

def add_two(x,y):
    return x + y
def mult_two(num1, num2):
    c = num1 * num2
    print(c)
while x == True:
    print('''Menu
          
    1) Add two numbers
    2) Multiply two numbers''') 
    user = int(input('Enter selections:'))
    num1 =  int(input('Enter a number: '))
    num2 =  int(input('Enter a number: '))
    if user == 1:
        a = add_two(num1, num2)
        print(a)
    elif user ==2:
        mult_two(num1, num2)
        
    else:
        print ('invalid')


