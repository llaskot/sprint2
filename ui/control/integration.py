# from data_process.integral_process import Differentiation_process
# from file_process.excel_process import Excel_process
import json

from data_process.integral_process import Integral_process
from ui.control.equalities import  Equalities
from ui.output.output import Output
import flet as ft

from ui.popup import Popup_integr


class Integration(Equalities):
    def __init__(self, page, output: Output, graph):
        super().__init__(page, output, graph)

    # def get_buttons(self):
    #     return [
    #         ft.ElevatedButton('Interpolation', on_click=self.process_interp,
    #                           height=30, color="white", width=120,
    #                           style=ft.ButtonStyle(
    #                               shape=ft.RoundedRectangleBorder(radius=5),
    #                               bgcolor={
    #                                   # ft.ControlState.DISABLED: "#535426",
    #                                   ft.ControlState.DEFAULT: "#020561"
    #                               }
    #                           )
    #                           ),
    #         ft.ElevatedButton('Approximation', on_click=self.process_approximation,
    #                           height=30, color="white", width=120,
    #                           style=ft.ButtonStyle(
    #                               shape=ft.RoundedRectangleBorder(radius=5),
    #                               bgcolor={
    #                                   # ft.ControlState.DISABLED: "#535426",
    #                                   ft.ControlState.DEFAULT: "#020561"
    #                               }
    #                           )
    #                           ),
    #     ]



    # def process_approximation(self, event):
        # interp = Differentiation_process(self.page.result)
        # print(interp.data)
        # interp.get_approximation_differential()
        # self.output.update_text(f'Approximation method')
        # self.output.set_tables_diff(self.page.result)
        # # self.graph.set_data(interp.data, "f'(x) approximation method")
        # self.graph.build_graph_diff()
        # self.graph.set_img()

    # def process_interp(self, event):
        # interp = Differentiation_process(self.page.result)
        # interp.get_interp_differential()
        # self.output.update_text(f'Interpolation method')
        # self.output.set_tables_diff(self.page.result)
        # # self.graph.set_data(interp.data, "f'(x) Interpolation method")
        # self.graph.build_graph_diff()
        # self.graph.set_img()

    def process_equality(self, event):
        integr = Integral_process(self.page.result["N"], self.page.result["a"], self.page.result["b"])
        res = integr.find_integrals(self.page.result["function"])
        func = {
            "function": self.page.result['function']
        }
        res = func | res
        print(json.dumps(res, indent=1, ensure_ascii=False))
        print(res)

        self.output.update_text(f"\nSolution for equality:\ny = {self.page.result['function']}")
        self.output.set_tables_diff(res)
        self.output.update_text(f' ')
        # self.graph.set_data(data, data["func"])
        # self.graph.build_graph()
        # self.graph.set_img()




    def func_name_upd(self):
        self.func_name.value = f"y = {self.page.result['function']}" \
            if self.page.result is not None else 'Select function'
        self.func_name.update()

    def open_popup(self, event):
        popup = Popup_integr(self.page, self.output, self.func_name_upd)
        popup.open()
