import flet as ft

from ui.control.equalities import Equalities
from ui.control.integration import Integration
# from ui.control.interpolation import Interpolation
from ui.graph.grapf import Graph
from ui.output.output import Output


def main(page: ft.Page):
    page.title = "Sprint 2"
    page.theme_mode = "dark"
    page.df = None
    page.result = None
    output = Output()
    graph = Graph('No name')
    graph.build_graph()
    interp = Equalities(page, output, graph)
    integr = Integration(page, output, graph)


    def open_diff(e):
        control.content.controls[0] = interp.control
        control.content.update()

    def open_int(e):
        control.content.controls[0] = integr.control
        control.content.update()

    res = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    bgcolor=ft.Colors.BLUE_100,
                    padding=2,
                    expand=2,
                    content=graph.img,
                    # visible=False
                ),
                ft.Container(
                    # bgcolor=ft.Colors.GREEN_100,
                    padding=2,
                    expand=1,
                    content=output.scroll_column,
                ),
            ]
        ),
        bgcolor=ft.Colors.GREY_900,
        padding=5,
        border_radius=5,
        expand=True
    )
    page.add(res)
    graph.set_img()

    control = ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                interp.control,
                ft.Container(
                    padding=10,
                    bgcolor=ft.Colors.BLUE_100,
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    output.clear
                                ]
                            ),
                            ft.Row(
                                controls=[
                                    ft.ElevatedButton('Diff Equalities',
                                                      height=30, color="white", width=120,
                                                      on_click=open_diff,
                                                      style=ft.ButtonStyle(
                                                          shape=ft.RoundedRectangleBorder(radius=5),
                                                          bgcolor={
                                                              # ft.ControlState.DISABLED: "#535426",
                                                              ft.ControlState.DEFAULT: "#136102"
                                                          }
                                                      )

                                                      ),
                                    ft.ElevatedButton('Integration',
                                                      height=30, color="white", width=120,
                                                      on_click=open_int,
                                                      style=ft.ButtonStyle(
                                                          shape=ft.RoundedRectangleBorder(radius=5),
                                                          bgcolor={
                                                              # ft.ControlState.DISABLED: "#535426",
                                                              ft.ControlState.DEFAULT: "#020561"
                                                          }
                                                      )

                                                      ),
                                ]
                            )

                        ],
                        width=250,

                    )
                )

            ]
        ),
        bgcolor=ft.Colors.TEAL,
        padding=5,
        border_radius=5,
        height=100,

    )
    page.add(control)




if __name__ == "__main__":
    ft.app(target=main)
