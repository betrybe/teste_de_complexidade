# flake8: noqa

def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)
    # Note that you want equal ^^^^^ not pivot
    else:
        return array


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_sorted = sort(list(first_string))
    second_sorted = sort(list(second_string))

    return first_sorted == second_sorted
