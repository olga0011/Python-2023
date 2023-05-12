"""Task 2 Decorators"""
import time


def timeit_decorator(func):
    '''Measure the execution time of a function and prints it to the console'''

    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        exec_time = end_time - start_time  # type: ignore
        print(exec_time)
        return exec_time

    return wrapper


@timeit_decorator
def test_function():
    '''Test function with an user input to get execution time longer than 0'''
    print("Please give me a string:")
    str4 = input()
    str_list = str4.split()
    longest = max(str_list, key=len)
    print(longest + " - " + str(len(longest)))


test_function()
