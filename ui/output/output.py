import flet as ft
import pandas as pd


class Output:
    def __init__(self):
        self.scroll_column = ft.Column(
            controls=[],
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
        self.clear = ft.Button('Clear',

                               height=30, color="white", width=250,
                               on_click=self.erase_history,
                               style=ft.ButtonStyle(
                                   shape=ft.RoundedRectangleBorder(radius=5),
                                   bgcolor={
                                       # ft.ControlState.DISABLED: "#535426",
                                       ft.ControlState.DEFAULT: "#210102"
                                   }
                               )

                               )

    def update_text(self, *update):
        current_output = []
        current_output.extend(update)
        text = ft.Text(
            '\n\n'.join(current_output),
            color=ft.Colors.GREEN_ACCENT_400,
            font_family="Courier New",
            size=18,
            selectable=True,
            expand=True,
        )
        # self.scroll_column.controls.clear()
        self.scroll_column.controls.append(text)
        self.scroll_column.scroll_to(offset=-1, duration=300)
        self.scroll_column.update()

    def set_tables(self, data: dict):
        name = None
        x_row = None
        y_row = []
        for key, val in data.items():
            if key == 'func':
                continue
            print(key, val)
            if key == 'x':
                x_row = [ft.DataColumn(ft.Text(key))] + [
                    ft.DataColumn(ft.Text(i, selectable=True, no_wrap=True, max_lines=1)) for i in val]
            else:
                yr = ft.DataRow(
                    cells=[ft.DataCell(ft.Text(key))] + [ft.DataCell(ft.Text(i, selectable=True,
                                                                             no_wrap=True, max_lines=1)) for i in val]
                )
                y_row.append(yr)

        table = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            controls=[
                ft.DataTable(
                    columns=x_row,
                    rows=y_row,
                    border=ft.border.all(2, ft.Colors.RED),
                )
            ])
        # self.scroll_column.controls.clear()
        self.scroll_column.controls.append(table)
        self.scroll_column.update()

    def set_tables_diff(self, data: dict):
        max_len = len(data['x_val'])
        table = ft.Row(
            scroll=ft.ScrollMode.AUTO,
            expand=True,
            controls=[
                ft.DataTable(
                    columns=[ft.DataColumn(ft.Text(data['x_name']))] + [ft.DataColumn(
                        ft.Text(data['x_val'][i] if i < len(data['x_val']) else '', selectable=True, no_wrap=True,
                                max_lines=1)) for i in range(max_len)],
                    rows=[
                        ft.DataRow(
                            cells=[ft.DataCell(ft.Text(ind))] + [ft.DataCell(
                                ft.Text(str(row[i]) if i < len(row) else '', selectable=True, no_wrap=True,
                                        max_lines=1)) for i in range(max_len)]
                        )
                        for row, ind in ((data['func_val'], data['func_name']),
                                         (data['analytics_val'], data['analytics_name']),
                                         (data['numeric_val'], data['numeric_name']))
                    ],
                )
            ])
        # self.scroll_column.controls.clear()
        self.scroll_column.controls.append(table)
        self.scroll_column.update()

    def erase_history(self, e):
        self.scroll_column.controls.clear()
        self.scroll_column.update()
