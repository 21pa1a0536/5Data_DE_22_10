#Problem Statement:  i have 100 functions for each function i want to find out the execution time.


import time
#1. Using Loops:

def sum_fun():
    sum1=0
    for i in range(1,100001):
        sum1+=i
    return sum1

def exe_time_loops(list_of_fun):
    for function in list_of_fun:
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"The execution time of \"{function.__name__}\" Function is {end_time-start_time:.6f}")

Fun_List = []

#Append all the functions to whom you want the Execution Time.
Fun_List.append(sum_fun)
exe_time_loops(Fun_List)

""" NOTED_POINT: Getting different execution time (Mostly at same Range i.e., 0.052, 0.049, 0.051 etc), everytime when we run the same code.
                 Due to OS Scheduling, Cache Effects etc i.e., if our computer is free, the code runs a bit faster, else a bit slower.
                 So Time differs for every execution.
"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------

#2. Using Decorators:

#Create a Wrapper Function
def exe_time_dec(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        Result = function(*args, **kwargs)
        end_time = time.time()
        print(f"The execution time of \"{function.__name__}\" Function is {end_time-start_time:.6f}")
        return Result
    return wrapper

#Now you can Add this Execution Time functionality as a Decorator to any of the function you want.
@exe_time_dec
def add_two_nums(a,b):
    sum1 = a+b
    return sum1

print(add_two_nums(5,3))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#3. Using timeit instead of time:
"""Why?
       timeit gives better accuracy for Smaller Eexcution results.
   Ehat it do?
       takes a function and number(which is number of times to run the function to get accurate execution time)
       Returns average of the time taken to run the function n number of times
"""
#Used for Small Execution Time Functions

import timeit
def sum_fun():
    sum1=0
    for i in range(1,100001):
        sum1+=i
    return sum1

def exe_time_loops(list_of_fun):
    for function in list_of_fun:
        result = timeit.timeit(function,number = 10)
        print(f"The execution time of \"{function.__name__}\" Function is {result:.6f}")

Fun_List = []

#Append all the functions to whom you want the Execution Time.
Fun_List.append(sum_fun)
exe_time_loops(Fun_List)


