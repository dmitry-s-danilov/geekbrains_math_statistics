# %% import modules

import numpy as np
from problem_1_lib import statistics

# %% define functions


def approximately_equal(x: float, y: float) -> bool:
    p = 6
    return round(x, p) == round(y, p)


def statistics_test(x: np.array) -> dict:
    return {
        'mean': x.mean(),
        'var': x.var(),
        'std': x.std(),
        'var_unbiased': x.var(ddof=1),
        'std_unbiased': x.std(ddof=1)
    }


# %% create an array

array = np.random.randint(low=1, high=100, size=10)

array_statistics = [
    statistics(list(array)),
    statistics_test(array)
]

# %% make a test

check_statistics = {
    key: approximately_equal(array_statistics[1][key], value)
    for key, value in array_statistics[0].items()
}

check_statistics_all = all(check_statistics.values())

print(check_statistics_all if check_statistics_all else check_statistics)
