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
  print("Invalid input! Please input a positive value")
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

def checking_Prime():       # Checking if the number is prime
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

def random_number():        # Random number generator + odd or even definer
    m = random.randint(10, 200)
    if m % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')
    print('The number:', m)
    
# random_number()

def listtraversing():       # Traversing through the list
    l1 = ['hello', 10, True, 10.3]
    for i in range(len(l1)):
        print(l1[i])
        print('\n')

# listtraversing()

def sum_list():     # Sum of all elemets in a list
    q = 0
    l2 = [100, 200, 2, 4, 123]
    for i in l2:
        q = q + i
    print(q)

# sum_list()

def max_min_list():
    l3 = [100, 23, 2323, 23, 9, 343, 123143, 545, 463, 342, 3231, 89890, 342]
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
    m1 = 1000000000
    for i in l3:
        if i < m1:
            m1 = i
        else: 
            continue
    print('The minimum of the list (Without using the min() function):', m1)

    # Maximum of the list without using the max() function
    m2 = 0
    for i in l3:
        if i > m2:
            m2 = i
        else:
            continue
    print('Max number in the list is:', m2)

#  max_min_list()

# 23/11/23 Class
def list_opperations():
    # Adding elements to the list using the append funtion
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'hello']
    print(l1)
    l1.append('world')
    print(l1)
    l1.insert(2, 'no') # Inserting into a certain index

    # Removing elements from the list (using the pop function)
    l1.pop(3)
    print(l1)

    # Removing elements from a list using the remove() function
    l1.remove(5)
    print(l1)


# list_opperations()

def finding_value_in_a_list():      # Finding a certain value in a list + the index of the element
    q = [12, 23, 44, 34, 543, 123, 343, 12, 12, 343]
    w = 0
    for i in q:
        if i == 123:
            print('It is here at the index:', w)
        else:
            pass
        w = w + 1

# finding_value_in_a_list()

def sum_list_2():         # Summing all the the elements of a list (Same as the funtion sum_list())
    t = [1, 2, 3, 4, 5, 6, 7, 8]
    r = 0
    for i in t:
        r += i
    print(r)

# sum_list_2()

def sum_half_list():
    q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l = len(q)/2
    m = 0
    for i in range(int(l)):
        m += i
    print(m)
    
# sum_half_list()
    
def sum_half_list_reverse():
    q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l = len(q)/2
    m = 0
    for i in range(-1 ,-int(l), -1):
        print(i)
        m += q[i]
    print(m)

# sum_half_list_reverse()

def rec_factorial(n):
    if n == 1:
        return 1
    return n*rec_factorial(n-1)

""" n = int(input('Enter a number: '))
print(rec_factorial(n)) """

def rec_example1(x):
    if x > 5:
        return
    rec_example1(x+1)
    print('Condition not met')
    

# rec_example1(0)

def sumlist_rec(a, i, s):
    if i == len(a):
        return s
    else:
        s = s + a[i]
    return sumlist_rec(a, i+1, s+1)

""" a = [1, 2, 3, 4, 5]
print(sumlist_rec(a, 0, 0)) """

# For the tower of Hanoi, n = 1, t(n) = 1. n = 2, t(n) = 3 and so on.

def TowerOfHanoi(n , s_pole, d_pole, i_pole):   # s is the first pole, d the second pole and i the third pole
    if n == 1:
        print("Move disc 1 from pole",s_pole,"to pole",d_pole)
        return
    TowerOfHanoi(n-1, s_pole, i_pole, d_pole)
    print("Move disc",n,"from pole",s_pole,"to pole",d_pole)
    TowerOfHanoi(n-1, i_pole, d_pole, s_pole)
 
""" n = 4   # When n = 4, there will be 15 + 1 + 15 moves, therefore 
TowerOfHanoi(n, 'A', 'C', 'B')
 """

def sorting():
    sl = [2, 3, 1, 6, 4]
    sl1 = []
    def sort():
        for i in range(len(sl)):
            minnum = min(sl)
            sl.remove(minnum)
            sl1.append(minnum)
        return sl1

    # print(sort())

    def recsort(qwe):   # Does not work
        if len(qwe) == 0:
            return
        else:
            q = min(qwe)
            qwe.remove(q)
            wer = qwe
            recsort(wer)

    # print(recsort(sl))
    
    def bubblesort(s):
        k = len(s)
        for i in range(k):
            for j in range(k-1):
                if s[j] > s[j+1]:
                    m = s[j]
                    s[j] = s[j+1]
                    s[j+1] = m
        return s
    # print(bubblesort(sl))

# sorting()

def swapping():
    o = [1, 2]
    p = o[0]
    o[0] = o[1]
    o[1] = p
    print(o)

# swapping()