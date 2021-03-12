from scipy.stats import norm, t
from functools import partial


def significance_interval(A, n=None):
    ppf = partial(t.ppf, df = n - 1) if n is not None else norm.ppf
    a = A / 2, 1 - A / 2    
    return ppf(a)


def confidence_interval(E, S, n, z_a):
    return [E - _ * S / n**.5 for _ in z_a[::-1]]


def alternative_hypothesis_1(z, A, n=None):
    ppf = partial(t.ppf, df = n - 1) if n is not None else norm.ppf
    a = A / 2, 1 - A / 2
    z_a = ppf(a)
    return z < z_a[0] or z_a[1] < z


def alternative_hypothesis_1_less(z, A, n=None):
    ppf = partial(t.ppf, df = n - 1) if n is not None else norm.ppf
    a = A
    z_a = ppf(a)
    return z < z_a


def alternative_hypothesis_1_more(z, A, n=None):
    ppf = partial(t.ppf, df = n - 1) if n is not None else norm.ppf
    a = 1 - A
    z_a = ppf(a)
    return z_a < z
