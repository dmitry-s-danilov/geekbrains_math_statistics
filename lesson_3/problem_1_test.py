# %%

import numpy as np
from problem_1_lib import statistics_1, statistics_2

# %%

# precision in decimal digits
precision = 6

# %%

array = np.random.randint(low=1, high=100, size=10)

array_statistics = [
    statistics_1(list(array)),
    statistics_2(array)
]

# %%

check_statistics = {
    key: round(array_statistics[1][key], precision) == round(value, precision)
    for key, value in array_statistics[0].items()
}

check_statistics_all = all(check_statistics.values())

print(check_statistics_all if check_statistics_all else check_statistics)
