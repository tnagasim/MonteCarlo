# %%
import numpy as np
from scipy.optimize import OptimizeResult


# %%
method_name = 'CanonicalMc'


class NoBetaError(OptimizeResult):
    def __init__(self):
        super().__init__(
            success=False,
            message='option in argumnet has not key beta.',
        )


class NoXDigitError(OptimizeResult):
    def __init__(self):
        super().__init__(
            success=False,
            message='option in argumnet has not key beta.'
        )


def next(x, digit):
    n = x.size
    i = np.random.randint(0, n)
    sign = np.random.randint(0, 1) * 2 - 1
    d = np.zeros(x.size)
    d[i] = sign * digit
    return x + d


# %%
def minimize(func, x0, args=(), method=method_name,
        jac=None, hess=None, hessp=None,
        bounds=None,
        constraints=(), tol=None, callback=None, options=None):
    if not 'beta' in options.keys():
        return NoBetaError()
    if not 'x_digit' in options.keys():
        return NoXDigitError()
    beta = options.beta
    e_last = func(x0, args)
    x_cur = next(x0, options.digit)
    return result

# %%
def func(x, args):
    return np.dot(x, x)

# %%
d = 1
x0 = np.ones(d)
