"""
Functions that summarize a list of numbers.

Meant to run after data_cleaning.py has already cleaned the raw data,
this keeps each module focused on one job, cleaning or summarizing,
instead of mixing both jobs into one long file.
"""


def total(numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def average(numbers):
    if not numbers:
        raise ValueError("cannot find average of an empty list")
    return total(numbers) / len(numbers)


def highest(numbers):
    return max(numbers)


def lowest(numbers):
    return min(numbers)
