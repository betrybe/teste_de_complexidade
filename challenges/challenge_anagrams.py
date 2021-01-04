def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    first_sorted = sorted(first_string)
    second_sorted = sorted(second_string)

    return first_sorted == second_sorted
