import math
import sympy as sp

x_var = sp.Symbol('x_var')

f_sym = {
    "expon": sp.exp(x_var),
    "sinus": sp.sin(x_var),
    "x^2": x_var * x_var,
    "x^3 + 2x^2 + 5": x_var**3 + 2*(x_var**2) + 5,
}


def super_func(func_name: str, x: float, lev: int = 0):
    expr = f_sym[func_name]
    derivative = sp.diff(expr, x_var, lev)
    func = sp.lambdify(x_var, derivative, modules='math')
    return func(x)


# if __name__ == '__main__':
#     from data_process.integral_process import Integral_process
#
#     integr = Integral_process(1000, 0, 5)
#     # print(integr.values)
#     # gen = integr.process_function(sqr)
#     # for i in range(4):
#     #     print(next(gen))
#     # integr.get_func_values(sqr)
#
#     # integr.find_integrals(sqr)
#     integr.find_integrals('x^3 + 2x^2 + 5')
