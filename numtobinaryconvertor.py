import math
import time
import datetime 


def num_to_binary_conversion():
    n = int(input('Enter number: '))
    m = bin(n).replace('0b', '')
    m1 = bin(n)
    print('The binary form of the number:', m)
    print('The number:', int(m1, 2))
    


num_to_binary_conversion()