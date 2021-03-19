import numpy as np
from scipy.stats import linregress
from functools import partial

from problem_1_lib import linregress_1, linregress_2, linregress_3
from problem_1_data import x, y


def dec_1(function, arguments):
    def wrapper(*args, **kwargs):
        kwargs_restricted = kwargs
        for argument in arguments:
            if argument in kwargs_restricted:
                del kwargs_restricted[argument]
        return function(*args, **kwargs_restricted)
    wrapper.__name__ = function.__name__
    return wrapper


def dec_2(function):
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)._asdict()
    wrapper.__name__ = function.__name__
    return wrapper


linregress = dec_2(dec_1(linregress, ['interception']))


round = partial(round, ndigits=10)


if __name__ == '__main__':

    test_functions = {
        True: [
            linregress,
            linregress_1,
            linregress_2,
            linregress_3
        ],
        False: [
            linregress_1,
            linregress_2,
            linregress_3
        ]
    }

    valid_functions = {
        True: test_functions[True][0],
        False: test_functions[False][0]
    }

    x = np.array(x)
    y = np.array(y)

    results = {
        intercept_key: {
            function.__name__: function(x, y, interception=intercept_key)
            for function in functions
        }
        for intercept_key, functions in test_functions.items()
    }

    checks = {
        intercept_key: {
            function_name: {
                result_key: round(
                    result_value -
                        intercept_results
                        [valid_functions[intercept_key].__name__]
                        [result_key]
                ) == 0
                for result_key, result_value
                in function_results.items()
            }
            for function_name, function_results
            in intercept_results.items()
            if function_name  is not valid_functions[intercept_key].__name__
        }
        for intercept_key, intercept_results
        in results.items()
    }

    for intercept_key, intercept_results in results.items():
        print(f"interception: {intercept_key}")
        for function_name, function_results in intercept_results.items():
            check = all(checks[intercept_key][function_name].values()) \
                if function_name in checks[intercept_key].keys() \
                else None

            print(
                f"{function_name}:",
                f"slope={function_results.get('slope'):.6f}",
                f"intercept={function_results.get('intercept'):.6f}",
                check if check is not None else ''
            )
