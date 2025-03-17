# import pytest

from defput import (
    factorial,
    is_prime,
    unique_el,
    sort_words,
)
def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(7) == 5040

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(5) == True
    assert is_prime(6) == False
    assert is_prime(7) == True
    assert is_prime(8) == False
    assert is_prime(9) == False
    assert is_prime(10) == False
    assert is_prime(11) == True
    assert is_prime(13) == True
    assert is_prime(15) == False
    assert is_prime(17) == True

def test_unique_el():
    assert set(unique_el([1, 2, 2, 3, 4, 4, 5])) == {1, 2, 3, 4, 5}
    assert set(unique_el(['a', 'b', 'c', 'b'])) == {'a', 'b', 'c'}
    assert set(unique_el([1, 1, 1, 1])) == {1}
    assert set(unique_el(['apple', 'banana', 'apple'])) == {'apple', 'banana'}
    assert set(unique_el([1, 2, 3, 4, 5, 6])) == {1, 2, 3, 4, 5, 6}

def test_sort_words():
    words = ['hello', 'world', 'python', 'java']
    result2 = sort_words(words)
    assert 4 in result2 and 'java' in result2[4]
    assert 5 in result2 and 'hello' in result2[5]
    assert 5 in result2 and 'world' in result2[5]
    assert 6 in result2 and 'python' in result2[6]
