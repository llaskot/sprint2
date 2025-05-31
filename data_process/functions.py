import sympy as sp

x_var = sp.Symbol('x_var')

f_sym = {
    "exp(-x)": sp.exp(-x_var),
    "sin(x)": sp.sin(x_var),
    "exp(-x^2)": sp.exp(-(x_var**2)),
    "exp(-4x)": sp.exp(-4*x_var),
    "sin(2x)": sp.sin(2*x_var),
    "exp(-3x^2)": sp.exp(-3*(x_var**2)),
    "exp(-4x-х^3)": sp.exp(-4*x_var-x_var**3)
}


def super_func(func_name: str, lev: int = 0):
    expr = f_sym[func_name]
    derivative = sp.diff(expr, x_var, lev)
    return sp.lambdify(x_var, derivative, modules='math')


