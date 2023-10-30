import math
import time
import pickle
import datetime
import turtle
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
