#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -=1
        print("Happy New Year!")
    pass

def square_integers(int_list):
    int_list = [int ** 2 for int in int_list]
    return int_list
    

def fizzbuzz():
    for num in range (1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
