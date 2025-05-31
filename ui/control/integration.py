from data_process.integral_process import Integral_process
from ui.control.equalities import Equalities
from ui.output.output import Output
from ui.popup import Popup_integr


class Integration(Equalities):
    def __init__(self, page, output: Output, graph):
        super().__init__(page, output, graph)

    def process_equality(self, event):
        integr = Integral_process(self.page.result["N"], self.page.result["a"], self.page.result["b"])
        res = integr.find_integrals(self.page.result["function"])
        func = {
            "function": self.page.result['function']
        }
        res = func | res
        self.output.update_text(f"\nSolution for equality:\ny = {self.page.result['function']}")
        self.output.set_tables_diff(res)
        self.output.update_text(f' ')

    def func_name_upd(self):
        self.func_name.value = f"y = {self.page.result['function']}" \
            if self.page.result is not None else 'Select function'
        self.func_name.update()

    def open_popup(self, event):
        popup = Popup_integr(self.page, self.output, self.func_name_upd)
        popup.open()
