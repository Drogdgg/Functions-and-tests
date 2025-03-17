def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def unique_el(lst):
    return list(set(lst))

def sort_words(words):
    s_words = sorted(words, key=len)
    result = {}
    for word in s_words:
        length = len(word)
        if length not in result:
            result[length] = [word]
        else:
            result[length].append(word)
    return result