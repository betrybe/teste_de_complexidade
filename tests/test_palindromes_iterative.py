from challenges.challenge_palindromes_iterative import is_palindrome_iterative
import timeit


def test_validar_se_a_palavra_e_um_palindromo_iterativo_retorna_true():
    word = "ANA"
    assert is_palindrome_iterative(word) is True
    word = "SOCOS"
    assert is_palindrome_iterative(word) is True
    word = "REVIVER"
    assert is_palindrome_iterative(word) is True


def test_validar_se_a_palavra_nao_e_um_palindromo_iterativo_retorna_false():
    word = "AGUA"
    assert is_palindrome_iterative(word) is False


def test_validar_se_nao_passar_palavra_iterativa_retorna_false():
    word = ""
    assert is_palindrome_iterative(word) is False


def test_validar_tempo_iterative():
    expect = ("from challenges.challenge_palindromes_iterative "
              "import is_palindrome_iterative")
    print("printou o tempo de iterative")
    print(timeit.timeit(f'is_palindrome_iterative("ANA")',
                        setup=f"{expect}"))
    print("printou o tempo de iterative")
    print("printou o tempo de iterative com varias execucoes")
    print(timeit.timeit(f'is_palindrome_iterative("ANA")',
                        setup=f"{expect}", number=10000000))
    print("printou o tempo de iterative com varias execucoes")
