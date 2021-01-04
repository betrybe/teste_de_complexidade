from challenges.challenge_palindromes_recursive import is_palindrome_recursive
import timeit


def test_validar_se_a_palavra_e_um_palindromo_retorna_true():
    word = "ANA"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is True
    word = "SOCOS"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is True
    word = "REVIVER"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is True


def test_validar_se_a_palavra_nao_e_um_palindromo_retorna_false():
    word = "AGUA"
    assert is_palindrome_recursive(word, 0, len(word) - 1) is False


def test_validar_se_nao_passar_palavra_retorna_false():
    word = ""
    assert is_palindrome_recursive(word, 0, len(word) - 1) is False


def test_validar_tempo_palindromo():
    expect = ("from challenges.challenge_palindromes_recursive "
              "import is_palindrome_recursive")
    print("printou o tempo de palindromo")
    print(timeit.timeit(f'is_palindrome_recursive("ANA", 0, len("ANA") - 1)',
                        setup=f"{expect}"))
    print("printou o tempo de palindromo")
    print("printou o tempo de palindromo com varias execucoes")
    print(timeit.timeit(f'is_palindrome_recursive("ANA", 0, len("ANA") - 1)',
                        setup=f"{expect}", number=10000000))
    print("printou o tempo de palindromo com varias execucoes")
