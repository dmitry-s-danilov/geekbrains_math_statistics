from scipy.stats import norm, t


def H1(z, A, n=None):
    a = A / 2, 1 - A / 2
    z_a = t.ppf(a, n - 1) if n is not None else norm.ppf(a)
    return z < z_a[0] or z_a[1] < z


def H1_less(z, A, n=None):
    z_a = t.ppf(A, n - 1) if n is not None else norm.ppf(A)
    return z < z_a


def H1_more(z, A, n=None):
    a = 1 - A
    z_a = t.ppf(a, n - 1) if n is not None else norm.ppf(a)
    return z_a < z
