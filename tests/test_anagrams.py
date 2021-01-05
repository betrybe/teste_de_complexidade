import timeit


def test_validar_tempo_anagrama():
    expect = ("from challenges.challenge_anagrams "
              "import is_anagram_selectionSort, is_anagram_insertionSort, "
              "is_anagram_bubbleSort, is_anagram_mergeSort, "
              "is_anagram_quickSort, "
              "is_anagram_sort")
    print("is_anagram_selectionSort")
    teste = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
             "sed do eiusmod tempor incididunt ut "
             "labore et dolore magna aliqua.")
    teste2 = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
              "do sed eiusmod tempor incididunt "
              "ut labore et dolore magna aliqua.")
    print(timeit.timeit(f'is_anagram_selectionSort("{teste}","{teste2}")',
                        setup=f"{expect}", number=10000))
    print(timeit.repeat(f'is_anagram_selectionSort("{teste}","{teste2}")',
                        setup=f"{expect}", number=10000, repeat=5))
    print("is_anagram_insertionSort")
    print(timeit.timeit(f'is_anagram_insertionSort("{teste}", "{teste2}")',
                        setup=f"{expect}", number=10000))
    print(timeit.repeat(f'is_anagram_insertionSort("{teste}", "{teste2}")',
                        setup=f"{expect}", number=10000, repeat=5))
    print("is_anagram_bubbleSort")
    print(timeit.timeit(f'is_anagram_bubbleSort("{teste}", "{teste2}")',
                        setup=f"{expect}", number=10000))
    print(timeit.repeat(f'is_anagram_bubbleSort("{teste}", "{teste2}")',
                        setup=f"{expect}", number=10000, repeat=5))
    print("is_anagram_mergeSort")
    print(timeit.timeit(f'is_anagram_mergeSort("{teste}", "{teste2}")',
                        setup=f"{expect}", number=10000))
    print(timeit.repeat(f'is_anagram_mergeSort("{teste}", "{teste2}")',
                        setup=f"{expect}", number=10000, repeat=5))
    print("is_anagram_sort")
    print(timeit.timeit(f'is_anagram_sort("{teste}", "{teste2}")',
                        setup=f"{expect}", number=10000))
    print(timeit.repeat(f'is_anagram_sort("{teste}", "{teste2}")',
                        setup=f"{expect}", number=10000, repeat=5))
