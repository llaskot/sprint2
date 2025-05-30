

f = {
    "-xy": lambda x, y: -x * y,
    "y+x": lambda x, y: y + x,
    "(3x-12x^2)y": lambda x, y: (3 * x - 12 * x ** 2) * y,
    "(4*x-12x^2)y": lambda x, y: (4 * x - 12 * (x ** 2)) * y,
}


if __name__ == "__main__":
    from data_process.eq_process import Diff_eq

    obj = Diff_eq(1, 2, 40, 2.5, f["(4*x-12x^2)y"])
    print(obj.h, obj.x)
    print(obj.euler())
    print(obj.runge_kutta4())
    print(obj.runge_kutta3())
    print(obj.runge_kutta2())