import numpy as np


def linregress_1(x, y, interception=True):
    try:
        if not(len(x) == len(y) and len(x) >= 2):
            raise Exception
        xx_mean = np.mean(x**2)
        if interception:
            x_mean = x.mean()
            x_var = xx_mean - x_mean ** 2
            if x_var:
                y_mean = y.mean()
                xy_mean = np.mean(x * y)
                xy_cov = xy_mean - x_mean * y_mean
                slope = xy_cov / x_var
                intercept = y_mean - x_mean * slope
            else:
                raise ZeroDivisionError
        else:
            if xx_mean:
                xy_mean = np.mean(x * y)
                slope = xy_mean / xx_mean
                intercept = 0
            else:
                raise ZeroDivisionError
    except Exception:
        slope, intercept = None, None
    except ZeroDivisionError:
        slope, intercept = None, None
    finally:
        return {
            'slope': slope,
            'intercept': intercept
        }


def linregress_2(x, y, interception=True):
    try:
        if not(len(x) == len(y) and len(x) >= 2):
            raise Exception
        if interception:
            x_var = x.var()
            if x_var:
                x_mean = x.mean()
                y_mean = y.mean()
                xy_cov = np.cov(x, y, bias=True)[0, 1]
                slope = xy_cov / x_var
                intercept = y_mean - x_mean * slope
            else:
                raise ZeroDivisionError
        else:
            xx_mean = np.mean(x * x)
            if xx_mean:
                xy_mean = np.mean(x * y)
                slope = xy_mean / xx_mean
                intercept = 0
            else:
                raise ZeroDivisionError
    except Exception:
        slope, intercept = None, None
    except ZeroDivisionError:
        slope, intercept = None, None
    finally:
        return {
            'slope': slope,
            'intercept': intercept
        }


def linregress_3(x, y, interception=True):
    try:
        if not(len(x) == len(y) and len(x) >= 2):
            raise Exception
        A_transpose = np.array([np.ones_like(x), x]) \
            if interception \
            else np.reshape(x, (1, -1))
        A_dot_A_transpose = np.dot(
            A_transpose,
            A_transpose.transpose()
        )
        if np.linalg.det(A_dot_A_transpose):
            w = np.dot(
                np.linalg.inv(A_dot_A_transpose),
                np.dot(A_transpose, y)
            )
            intercept, slope = w if interception else (0, w[0])
        else:
            raise ZeroDivisionError
    except Exception:
        slope, intercept = None, None
    except ZeroDivisionError:
        slope, intercept = None, None
    finally:
        return {
            'slope': slope,
            'intercept': intercept
        }
