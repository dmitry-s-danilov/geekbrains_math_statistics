import numpy as np


def covariance(x_arg, y_arg):
    x, y = np.array(x_arg), np.array(y_arg)
    return np.mean((x - x.mean()) * (y - y.mean()))


def correlation_coefficient(x_arg, y_arg):
    x, y = np.array(x_arg), np.array(y_arg)
    return np.mean((x - x.mean()) * (y - y.mean())) / (x.var() * y.var())**0.5
