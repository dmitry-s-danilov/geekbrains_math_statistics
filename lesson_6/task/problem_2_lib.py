from scipy.stats import norm, t
from functools import partial


def significance_interval(A, n=None):
    ppf = partial(t.ppf, df = n - 1) if n is not None else norm.ppf
    a = A / 2, 1 - A / 2    
    return ppf(a)


def confidence_interval(E, S, n, z_a):
    return [E - _ * S / n**.5 for _ in z_a[::-1]]
