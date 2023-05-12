"""Task 3 Best Practices"""

numbers = [30, 8, 5, 2, 10, 33, 1, 0, 77]


def get_sum_of_even_numbers(numbers):
    """
    Take a list of integers as input and returns the sum of all even numbers in the list.

    Arguments:
    numbers - a list of all numbers.

    Returns:
    the sum of all even numbers of the list.
    """
    total = 0  # initialize a results variable
    try:
        for i in numbers:  # loop through each element of the list
            if not i % 2:  # test for even numbers
                total += i
        print(total)
        return total
    except TypeError:
        print("That was not a valid number")
        return None


get_sum_of_even_numbers(numbers)
