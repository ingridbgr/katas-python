from kata1 import *

def test_numeros_pares(): 

    result = numeros_pares()
    expected = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

    assert result == expected

def test_numeros_impares(): 

    result = numeros_impares()
    expected = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]

    assert result == expected

def test_numeros_primos(): 

    result = numeros_primos()
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    assert result == expected

def test_numeros_divisiveis_5():

    result = numeros_divisiveis_5()
    expected = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

    assert result == expected


def test_numeros_perfeitos():

    result = numeros_perfeitos()
    expected = [1, 4, 9, 16, 25, 36, 49, 64, 81]

    assert result == expected

def test_numeros_fibonacci():

    result = numeros_fibonacci()
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    assert result == expected