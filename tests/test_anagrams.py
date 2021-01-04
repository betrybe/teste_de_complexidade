from challenges.challenge_anagrams import is_anagram
import timeit


def test_validar_se_as_palavras_nao_sao_um_anagrama():
    first_string = "pedra"
    second_string = "perdaaa"
    assert is_anagram(first_string, second_string) is False


def test_validar_se_as_palavras_sao_um_anagrama():
    first_string = "pedra"
    second_string = "perda"
    assert is_anagram(first_string, second_string) is True


def test_validar_se_passar_primeira_palavra_em_branco_retorna_false():
    first_string = ""
    second_string = "perda"
    assert is_anagram(first_string, second_string) is False


def test_validar_se_passar_segunda_palavra_em_branco_retorna_false():
    first_string = "pedra"
    second_string = ""
    assert is_anagram(first_string, second_string) is False


def test_validar_tempo_anagrama():
    expect = ("from challenges.challenge_anagrams"
              "import is_anagram")
    print("printou o tempo de anagrama")
    print(timeit.timeit('is_anagram("pedra", "pedro")',
                        setup=expect))
    print("printou o tempo de anagrama")
    print("printou o tempo de anagrama com varias execucoes")
    print(timeit.timeit('is_anagram("pedra", "pedro")',
                        setup=expect, number=10000000))
    print("printou o tempo de anagrama com varias execucoes")
