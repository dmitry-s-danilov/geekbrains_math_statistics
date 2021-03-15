import numpy as np


def covariance(x, y):
    return np.mean((x - x.mean()) * (y - y.mean()))


def correlation_coefficient(x, y):
    return np.mean((x - x.mean()) * (y - y.mean())) / (x.var() * y.var())**0.5
