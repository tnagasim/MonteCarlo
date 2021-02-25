# %%
import numpy as np
from scipy.optimize import OptimizeResult


# %%
method_name = 'CanonicalMc'
tol_default = 1.e-3


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
    if tol is None:
        tol = tol_default
    beta = options.beta
    e0 = func(x0, args)
    if 'max_loop' in options.keys():
        max_loop = options[max_loop]
    for _ in range(max_loop)
        x1 = next(x0, options.digit)
        e1 = func(x1, args)
        delta = beta * (e1 - e0)
        if delta > 0:
            r = np.random.rand()
            p = np.exp(-delta)
            if r > p:
                continue
        if abs(e1 - e0) < tol:
            break
        x0 = x1
        e0 = e1

    return result

# %%
def func(x, args):
    return np.dot(x, x)

# %%
d = 1
x0 = np.ones(d)
