import timeit


def test_validar_tempo_anagrama():
    expect = ("from challenges.challenge_anagrams "
              "import is_anagram_sort")
    teste = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
             "sed do eiusmod tempor incididunt ut "
             "labore et dolore magna aliqua.")
    teste2 = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
              "do sed eiusmod tempor incididunt "
              "ut labore et dolore magna aliqua.")
    print("printou o anagrama")
    assert timeit.timeit(f'is_anagram_sort("{teste}", "{teste2}")',
                         setup=f"{expect}", number=10000) <= 2
