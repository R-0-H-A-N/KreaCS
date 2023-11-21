import math
import time
import pickle
import datetime
import turtle
from decimal import Decimal
import random # This is the random module

# import pandas
# import matplotlib

# Most of the current imports are not doing much and are unnecessary but i do like to add them anyway as i see it as a good practice.
# Do not worry about most of them as they are not really required unless you want to do very particular things.


print(math.pi) # Printing pi. I use it to figure out if there is an error before this. If there is, this will not run.
# If it does show, then it means the error is after this, making it easy to debug. 

# I shall be using funcitons as blocks to talk about and showcase different things. If you have never done functions in programming before, don't worry. 
# A function is a block of code which can be called in the code when we want it to run. For example, if i want to write the code for something but not run it immediately, i can put it in a function and run the funtion when i want to run it. 

def addingBinaryNUmbers():
    print(
        " Adding numbers through binary can be done both via the binary form or via converting to numbers, \n adding and then converting the result to binary\n"
    )
    # Adding of Binary numbers
    print(" Example: \n 10 + 12 = 22 \n 1010 + 1100 = 10110")

    print(" 15 + 16 = 31 \n 1111 + 10000 = 11111 == 1 + 2 + 4 + 8 + 16 = 31")

# addingBinaryNUmbers()

def loopsExamples():
    for i in range(10):
        print("e")

    a = 10
    while a > 0:
        print("r")
        a -= 1

# loopsExamples()

def turtleintro():
    # Let us now talk about turtle
    mp = turtle.Turtle() # Here mp is a variable that stores the turtle.Turtle() function which allows us to call from the turtle library.
    mp.forward(100) # Tells the turtle to move forward by 100 pixels
    mp.back(100) # Tells teh turtle to move back by 100 pixels
    mp.left(90) # Tells the turtle to rotate left by 90 degrees
    mp.right(90) # Tells the turtle to rotate right by 90 degrees

    # Feel free to experiment with the code. 
    # I would recommend getting comfortable with functions as well as it will help a lot in the future. 

# turtleintro()

def turtlesomewhatadvanced():
    mw = turtle.Screen() # Setting up screen to be able to change the backgroud color
    mw.bgcolor("blue") # Changing the backgroud for aesthetic purposes
    mp = turtle.Turtle() # Initialising the turtle module and setting it the variable mp, from this point forward mp will be used to perform actions on the turtle
    mp.speed(30) # Setting the speed of the turtle
    n = 18
    for i in range(5):
        for i in range(n):
            mp.forward(20)
            mp.right(20)
        for i in range(n):
            mp.forward(20)
            mp.left(20)
        mp.right(20)
        for i in range(n):
            mp.forward(20)
            mp.right(20)
        for i in range(n):
            mp.forward(20)
            mp.left(20)
        mp.right(20)
    mp.left(20)
    mp.forward(200)

    for i in range(5):
        for i in range(n):
            mp.forward(20)
            mp.right(20)
        for i in range(n):
            mp.forward(20)
            mp.left(20)
        mp.right(20)
        for i in range(n):
            mp.forward(20)
            mp.right(20)
        for i in range(n):
            mp.forward(20)
            mp.left(20)
        mp.right(20)
    mp.left(20)
    mp.forward(400)
    for i in range(5):
        for i in range(n):
            mp.forward(20)
            mp.right(20)
        for i in range(n):
            mp.forward(20)
            mp.left(20)
        mp.right(20)
        for i in range(n):
            mp.forward(20)
            mp.right(20)
        for i in range(n):
            mp.forward(20)
            mp.left(20)
        mp.right(20)

    time.sleep(5)
    turtle.done()

# turtlesomewhatadvanced()

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
     result = 0
  return result

# tri_recursion(6)

def list_sum(n_list):
    if len(n_list) == 1:
        return n_list[0]
    else:
        return n_list[0] + list_sum(n_list[1:])
    
# print(list_sum([1, 2, 3, 5, 6, 12, 13]))

def forloopAdding(l1):
    a = 0
    for i in l1:
        a += i
    print(a)

# forloopAdding([1, 2, 3, 5, 6, 12, 13])

def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
 
n_terms = 11
 
# check if the number of terms is valid
""" if n_terms <= 0:
  print("Invalid input ! Please input a positive value")
else:
  print("\nFibonacci series:")
  print(recursive_fibonacci(n_terms))
for i in range(n_terms + 1):
    print(recursive_fibonacci(i)) """

def variable_type():
    a = 1.0000000000000000000000000000000000000000000000000000000000000000001
    print(type(a))
    print(a)
    int(input('Brrrr: ')) # This input will only allow for integer data values and throw and error if thats not the case
    input('Brrrrrrrr: ') # This input will allow for any input and store it as a string
    print(Decimal(a)) # Using the Decimal library
    print(type(Decimal(a)))

# variable_type()

def date_2_11_23():
    age = int(input('Enter your age here: '))
    region = input('Enter your region here: ')
    if age > 18 and region == 'tada':
        print('congrats, you are eligible to vote')
        if age > 70:
            print('Do you need any help?')
            help_age = input('Yes(y)/No(n): ')
            if help_age == 'y':
                print('*insert helpful things here')
            elif help_age == 'n':
                print('Okay, you do not need any help')
            else:
                print('Invalid input')
    else:
        print('You are not eligible')
        h = 18 - age
        print('please try again in: ',h , 'years')

# date_2_11_23()

def backward_couting():
    n = 10
    for i in range(0, -n-1, -1):
        print(i)

# backward_couting()

def factorialOfaNumber():
    n = int(input('Enter a number you would like to take a factorial for: '))
    m = 1
    while n > 0:
        m = m * n
        n = n - 1 
    print(m)

# factorialOfaNumber()

def adding_allDigits_Of_a_Number():
    n = int(input('Enter the number: '))
    m = str(n)
    j = 0
    for i in m:
        j = j + int(i)
    print(j)

# addingallDigitssOfaNumber()

def remainder_Devision_Method_for_Adding_Digits():
    n = int(input('Enter the number you would like to add: '))
    sumDigits = 0
    while n > 0:
        b = n % 10
        sumDigits = sumDigits + b
        n = int(n / 10)
    print(sumDigits)

# remainder_Devision_Method_for_Adding_Digits()

def checking_Prime():
    n = int(input('Enter a number (>=2): '))
    m = 0
    for i in range(1, n+1):
        if n % i == 0:
            m += 1
        else:
            continue
    if m > 2:
        print('Number is not prime')
    else:
        print('Number is prime')

# checking_Prime()

def random_number():
    m = random.randint(10, 200)
    if m % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')
    print('The number:', m)
    
# random_number()

def listtraversing():
    l1 = ['hello', 10, True, 10.3]
    for i in range(len(l1)):
        print(l1[i])
        print('\n')

# listtraversing()

def sum_list():
    q = 0
    l2 = [100, 200, 2, 4, 123]
    for i in l2:
        q = q + i
    print(q)

# sum_list()

def max_min_list():
    l3 = [100, 23, 2323, 23, 9]
    print('The max of the list (Using the max() funtion):', max(l3))
    print('The min of the list (Using the min() funtion):', min(l3))

    # Using the long method
    m = 0
    for i in l3:
        if i > m:
            m = i
        else: 
            continue
    print('The max of the list (Without using the max() funtion):', m)

    # lenght of the list without using len()
    s = 0
    for i in l3:
        s += 1
    print('The lenght of the list (without using the len() funtion):', s)

    # Minimum of a list wihout using the min() function
    m1 = 100000
    for i in l3:
        if i < m1:
            m1 = i
        else: 
            continue
    print('The minimum of the list (Without using the min() function):', m1)

#  max_min_list()