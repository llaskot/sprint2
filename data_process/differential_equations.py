f = {
    "-xy": lambda x, y: -x * y,
    "y+x": lambda x, y: y + x,
    "(3x-12x^2)y": lambda x, y: (3 * x - 12 * (x ** 2)) * y,
    "(4x-12x^2)y": lambda x, y: (4 * x - 12 * (x ** 2)) * y,
    "у+2х": lambda x, y: y + 2 * x,
    "(3x−11x^2)y ": lambda x, y: (3 * x - 11 * (x ** 2)) * y,
    "3у+х": lambda x, y: 3 * y + x,
}


