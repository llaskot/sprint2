class Diff_eq:
    def __init__(self, a: float, b: float, m: int, y0: float, func):
        self.a = a
        self.b = b
        self.m = m
        self.n = m + 1
        self.h = (b - a) / m
        self.func = func
        self.x = [a + n * self.h for n in range(self.n)]
        self.y0 = y0

    def euler(self):
        res = [self.y0]
        for x in self.x[:-1]:
            res.append(res[-1] + self.h * self.func(x, res[-1]))
        return res

    def runge_kutta4(self):
        res = [self.y0]
        for x in self.x[:-1]:
            r1 = self.h * self.func(x, res[-1])
            r2 = self.h * self.func((x + self.h / 2), (res[-1] + r1 / 2))
            r3 = self.h * self.func((x + self.h / 2), (res[-1] + r2 / 2))
            r4 = self.h * self.func((x + self.h), (res[-1] + r3))
            res.append(res[-1] + (r1 + 2 * r2 + 2 * r3 + r4) / 6)
        return res

    def runge_kutta3(self):
        res = [self.y0]
        for x in self.x[:-1]:
            r1 = self.func(x, res[-1])
            r2 = self.func((x + self.h / 2), (res[-1] + (self.h / 2) * r1))
            r3 = self.func((x + self.h), (res[-1] - self.h * r1 + 2 * self.h * r2))
            res.append(res[-1] + (self.h / 6) * (r1 + 4 * r2 + r3))
        return res

    def runge_kutta2(self):
        res = [self.y0]
        for x in self.x[:-1]:
            r1 = self.func(x, res[-1])
            r2 = self.func((x + self.h), (res[-1] + self.h * r1))
            res.append(res[-1] + (self.h / 2) * (r1 + r2))
        return res
