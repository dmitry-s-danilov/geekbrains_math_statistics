import numpy as np


def statistics_1(x: list) -> dict:
    n = len(x)

    # expected value
    # математическое ожидание
    Ex = sum(x) / n

    # variance
    # дисперсия
    Dx = sum([(_ - Ex) ** 2 for _ in x]) / n

    # standard deviation
    # cреднеквадратическое отклонение
    Sx = Dx ** .5

    # unbiased variance
    # несмещённая дисперсия
    D0x = n / (n - 1) * Dx

    # unbiased standard deviation
    # несмещённое cреднеквадратическое отклонение
    S0x = D0x ** .5

    return {
        'mean': Ex,
        'var': Dx,
        'std': Sx,
        'var_unbiased': D0x,
        'std_unbiased': S0x
    }


def statistics_2(x: np.array) -> dict:
    return {
        'mean': x.mean(),
        'var': x.var(),
        'std': x.std(),
        'var_unbiased': x.var(ddof=1),
        'std_unbiased': x.std(ddof=1)
    }
