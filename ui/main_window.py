import flet as ft
from data_process.decorators import call_logging
from ui.control.equalities import Equalities
from ui.control.integration import Integration
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
    pict = ft.Container(
        bgcolor=ft.Colors.BLUE_100,
        padding=2,
        expand=2,
        content=graph.img,
    )

    @call_logging
    def open_diff(e):
        pict.visible = True
        integ_btn.bgcolor = "#020561"
        integ_btn.style.side = None
        diff_btn.bgcolor = ft.Colors.GREEN_500
        diff_btn.style.side = ft.BorderSide(3, ft.Colors.DEEP_ORANGE_900)
        pict.update()
        control.content.controls[0] = interp.control
        control.content.update()

    def open_int(e):
        pict.visible = False
        integ_btn.bgcolor = ft.Colors.BLUE_700
        integ_btn.style.side = ft.BorderSide(3, ft.Colors.DEEP_ORANGE_900)
        diff_btn.bgcolor = "#136102"
        diff_btn.style.side = None
        pict.update()
        control.content.controls[0] = integr.control
        control.content.update()

    diff_btn = ft.ElevatedButton('Diff Equalities',
                                 height=30, color="white", width=120,
                                 on_click=open_diff,

                                 style=ft.ButtonStyle(
                                     side=ft.BorderSide(3, ft.Colors.DEEP_ORANGE_900),
                                     elevation={
                                         None: 100,
                                         ft.ControlState.PRESSED: 0,
                                         ft.ControlState.HOVERED: 4
                                     },
                                     shape=ft.RoundedRectangleBorder(radius=5),
                                     bgcolor=ft.Colors.GREEN_500
                                     # bgcolor="#136102",
                                 )

                                 )

    integ_btn = ft.ElevatedButton('Integration',
                                  height=30, color="white", width=120,
                                  on_click=open_int,

                                  style=ft.ButtonStyle(
                                      side=None,
                                      # side=ft.BorderSide(3, ft.Colors.DEEP_ORANGE_900),
                                      elevation={
                                          None: 100,
                                          ft.ControlState.PRESSED: 0,
                                          ft.ControlState.HOVERED: 4
                                      },
                                      shape=ft.RoundedRectangleBorder(radius=5),
                                      bgcolor="#020561",
                                      # ft.Colors.BLUE_700,
                                  )

                                  )

    res = ft.Container(
        content=ft.Row(
            controls=[
                pict,
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
                                    diff_btn, integ_btn,
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
