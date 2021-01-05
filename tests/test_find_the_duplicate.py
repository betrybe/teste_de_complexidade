from challenges.challenge_find_the_duplicate import find_duplicate
import timeit


def test_validar_se_encontra_numeros_repetidos():
    nums = [1, 3, 4, 2, 2]
    assert find_duplicate(nums) == 2
    nums = [3, 1, 3, 4, 2]
    assert find_duplicate(nums) == 3
    nums = [1, 1]
    assert find_duplicate(nums) == 1
    nums = [1, 1, 2]
    assert find_duplicate(nums) == 1
    nums = [3, 1, 2, 4, 6, 5, 7, 7, 7, 8]
    assert find_duplicate(nums) == 7


def test_validar_se_retorna_false_quando_nao_envia_valores():
    nums = []
    assert find_duplicate(nums) is False


def test_validar_se_retorna_false_quando_envia_string():
    nums = ['a', 'b']
    assert find_duplicate(nums) is False


def test_validar_se_retorna_false_quando_nao_ha_repeticao():
    nums = [1, 2]
    assert find_duplicate(nums) is False


def test_validar_se_retorna_false_quando_passa_um_numero():
    nums = [1]
    assert find_duplicate(nums) is False


""" def test_validar_se_retorna_false_quando_passa_numero_negativo():
    nums = [-1, -1]
    assert find_duplicate(nums) is False """


def test_validar_tempo_duplicate():
    expect = ("from challenges.challenge_find_the_duplicate "
              "import find_duplicate")
    nums = [1, 3, 4, 2, 2]
    print("printou o tempo de duplicate")
    print(timeit.timeit(f'find_duplicate({nums})',
                        setup=f"{expect}"))
    print(timeit.repeat(f'find_duplicate({nums})',
                    setup=f"{expect}",repeat=5))
    print("printou o tempo de duplicate")
    print("printou o tempo de duplicate com varias execucoes")
    print(timeit.timeit(f'find_duplicate({nums})',
                        setup=f"{expect}", number=10000000))
    print(timeit.repeat(f'find_duplicate({nums})',
                        setup=f"{expect}", number=10000000, repeat=5))
    print("printou o tempo de duplicate com varias execucoes")
