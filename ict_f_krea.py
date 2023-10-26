import math
import time
import pickle
import datetime
import turtle

# import pandas

# import matplotlib

dict1 = {}


def b1w():
    o = open("file.dat", "wb")
    l = int(input("Enter the number of letters or numbers: "))
    l1 = []
    for i in range(l):
        m = input("Enter number or letter: ")
        l1.append(m)
    pickle.dump(l1, o)
    o.close()


def b1r():
    o = open("file.dat", "rb")
    f = pickle.load(o)
    print(f)

    o.close()


# b1w()
# b1r()

print(math.pi)


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


def turtlething():
    mw = turtle.Screen()
    mw.bgcolor("blue")
    mp = turtle.Turtle()
    mp.speed(30)
    a = 0
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


# turtlething()
