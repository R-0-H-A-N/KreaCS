import math
import time
import datetime 


def num_to_binary_conversion():
    n = int(input('Enter number: '))
    m = bin(n).replace('0b', '')
    print(m)

    
num_to_binary_conversion()    