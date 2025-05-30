import asyncio

from data_process.decorators import call_logging, log_thread_async
from data_process.functions import super_func


class Integral_process:
    def __init__(self, steps: int, a: float, b: float):
        self.steps_qty = steps
        self.a = a
        self.b = b
        self.step = 0
        self.values = self.obtain_values()

    def obtain_values(self):
        try:
            step = (self.b - self.a) / self.steps_qty
            self.step = step
            res = []
            next_el = self.a
            i = 0
            while next_el < self.b and i < self.steps_qty:
                res.append(next_el)
                i += 1
                next_el = self.a + i * step
            res.append(self.b)
            return res
        except ZeroDivisionError as e:
            print(f"ERROR: step's number must not be 0\n{e}")
            return []

    def __process_function(self, func):
        for val in self.values:
            yield func(val)

    # @call_logging
    def __get_func_values(self, func):
        res = []
        gen = self.__process_function(func)
        for val in gen:
            res.append(val)
        return res

    @call_logging
    def find_integrals(self, func_name: str):
        def func(x):
            return super_func(func_name, x)

        def func_2(x):
            return super_func(func_name, x, 2)

        def func_4(x):
            return super_func(func_name, x, 4)

        fuc_values = self.__get_func_values(func)
        max_rect = max(fuc_values)
        max_trap = max(self.__get_func_values(func_2))
        max_simps = max(self.__get_func_values(func_4))
        tolerance_rect = self.step ** 2 * max_rect * (self.b - self.a) / 24
        tolerance_trap = -1 * self.step ** 2 * max_trap * (self.b - self.a) / 12
        tolerance_simps = self.step ** 4 * max_simps * (self.b - self.a) / 180

        async def inner():
            return await asyncio.gather(
                self.left_rect(fuc_values, tolerance_rect),
                self.right_rect(fuc_values, tolerance_rect),
                self.center_rect(func, tolerance_rect),
                self.trapezoidal(fuc_values, tolerance_trap),
                self.simps(func, tolerance_simps)

            )

        left, right, center, trapezoidal, simpson = asyncio.run(inner())

        return {
            'left_rect': left,
            'right_rect': right,
            'center_rect': center,
            'trapezoidal': trapezoidal,
            'simpson': simpson
        }

    @log_thread_async
    async def simps(self, func, tolerance: float):
        if self.steps_qty % 2 != 0:
            N = self.steps_qty // 2
        else:
            N = (self.steps_qty - 1) // 2

        h = (self.b - self.a) / (2 * N)

        x_even = [self.a + 2 * n * h for n in range(1, N)]
        x_odd = [self.a + (2 * n - 1) * h for n in range(1, N + 1)]

        return h / 3 * (
                func(self.a) +
                func(self.b) +
                4 * sum(func(x) for x in x_odd) +
                2 * sum(func(x) for x in x_even) +
                tolerance
        )

    @log_thread_async
    async def trapezoidal(self, f_vals: list, tolerance: float):

        return self.step * (f_vals[0] + f_vals[-1]) / 2 + self.step * sum(f_vals[1:-1]) + tolerance

    @log_thread_async
    async def left_rect(self, f_vals: list, tolerance: float):
        return sum(f_vals[:-1]) * self.step + tolerance

    @log_thread_async
    async def right_rect(self, f_vals: list, tolerance: float):
        await asyncio.sleep(0)
        return sum(f_vals[1:]) * self.step + tolerance

    @log_thread_async
    async def center_rect(self, func, tolerance: float):
        return sum([func((x + self.step / 2)) for x in self.values[:-1]]) * self.step + tolerance
