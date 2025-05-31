import time

import flet as ft

from data_process.decorators import call_logging
from data_process.eq_process import Diff_eq
# from file_process.excel_process import Excel_process
from ui.graph.grapf import Graph
from ui.output.output import Output
from ui.popup import Popup_integr
from ui.popup_differ import Popup_differ
from data_process.differential_equations import f as dif_equal_name


class Equalities:
    def __init__(self, page, output: Output, graph):
        self.page = page
        self.output = output
        self.graph = graph
        self.btn_manual_input = ft.IconButton(ft.Icons.KEYBOARD, on_click=self.open_popup)
        self.buttons = self.get_buttons()
        self.func_name = ft.Text('Select function', size=22)

        self.control = ft.Container(
            expand=True,
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    padding=-3,
                                    content=ft.Row(
                                        controls=[
                                            ft.Text('Manual input  ', size=20),
                                            self.btn_manual_input,
                                        ]
                                    )
                                ),

                                ft.Container(
                                    content=self.func_name
                                )

                            ]
                        )
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=self.buttons
                        )
                    ),

                ],

            ),
            bgcolor="#4a4447",
            padding=10

        )

    def get_buttons(self):
        return [
            ft.ElevatedButton('Solve', on_click=self.process_equality,
                              height=30, color="white", width=120,
                              style=ft.ButtonStyle(
                                  shape=ft.RoundedRectangleBorder(radius=5),
                                  bgcolor={
                                      # ft.ControlState.DISABLED: "#535426",
                                      ft.ControlState.DEFAULT: "#136102"
                                  }
                              )

                              ),
        ]

    def process_equality(self, event):
        iq = Diff_eq(self.page.result['a'], self.page.result['b'], self.page.result['N'],
                     self.page.result['y0'], dif_equal_name[self.page.result['function']])

        data = {
            "func": self.page.result['function'],
            "x": iq.x,
            "y Euler": iq.euler(),
            "y Runge-Kutta 2": iq.runge_kutta2(),
            "y Runge-Kutta 3": iq.runge_kutta3(),
            "y Runge-Kutta 4": iq.runge_kutta4(),
        }
        self.output.update_text(f"\nSolution for equality:\ny' = f(x,y) = {self.page.result['function']}")
        self.output.set_tables(data)
        self.output.update_text(f' ')
        self.graph.set_data(data, data["func"])
        self.graph.build_graph()
        self.graph.set_img()

    def open_popup(self, event):
        popup = Popup_differ(self.page, self.output, self.func_name_upd)
        popup.open()

    @call_logging
    def func_name_upd(self):
        self.func_name.value = f"y' = f(x, y) = {self.page.result['function']}" \
            if self.page.result is not None else 'Select function'
        self.func_name.update()
