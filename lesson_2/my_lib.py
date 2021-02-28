from math import factorial, exp


def my_combinations(n, k):
    return int(factorial(n) / factorial(k) / factorial(n - k))


def my_binom(k, n, p):
    return my_combinations(n, k) * p**k * (1 - p)**(n - k)


def my_poisson(k, mu):
    return exp(-mu) * mu**k / factorial(k)
