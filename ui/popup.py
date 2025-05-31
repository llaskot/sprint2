import json

import flet as ft
import pandas as pd
import math

from ui.output.output import Output
from data_process.functions import f_sym as functions


class Popup_integr:
    def __init__(self, page, output: Output, upd):
        self.output = output
        # self.graph = graph
        self.a = None
        self.b = None
        self.n = None
        # self.y0 = None
        self.func = None
        self.page = page
        self.dialog = None  # Пока нет попапа
        self.upd = upd

        self.drp = ft.Dropdown(
            value="1",
            options=[ft.DropdownOption(key=key, text=f' {key} ') for key in functions],
        )

        self.values_fields = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(f'Function:'),
                            self.drp,
                            ft.Text(f'   a = '),
                            self.create_new_textfield(),
                            ft.Text(f'   b = '),
                            # self.create_new_textfield(),
                            # ft.Text(f'   y0 = '),
                            self.create_new_textfield(),
                            ft.Text(f"   Value's number ="),
                            self.create_new_textfield(),

                        ]
                    )
                )
            ],
            scroll=ft.ScrollMode.AUTO
        )
        self.scroll_column = ft.Column(
            controls=[
                self.create_fields_column(),
                ft.Text(''),
            ],
            scroll=ft.ScrollMode.AUTO
        )

    def get_data(self):
        res = {
            'function': self.func,
            'a': self.a,
            'b': self.b,
            'N': self.n,
        }
        print(res)
        self.page.result = res
        self.page.df = 'aaaa'

    def open(self, e=None):  # e=None для вызова вручную
        self.create_popup()
        self.dialog.open = True
        self.page.update()

    def cancel(self, e):
        self.dialog.open = False
        self.page.update()
        self.dialog = None

    def create_fields_column(self):
        return self.values_fields

    def create_new_textfield(self):
        return ft.TextField(
            # value="0",
            width=70,
            keyboard_type=ft.KeyboardType.NUMBER,
            input_filter=ft.InputFilter(
                regex_string=r"^-?\d*\.?\d*$",  # Разрешает: -, ., цифры
                allow=True,
                replacement_string=""  # Запрещает невалидные символы
            ),
            max_length=7,
            text_align=ft.TextAlign.CENTER,
            height=40,
            text_size=13,
            content_padding=ft.Padding(0, 4, 0, 0),

        )

    def create_popup(self):
        """Создает попап"""
        self.dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Fill in a data"),
            content=ft.Row(
                controls=[
                    ft.Container(
                        content=
                        self.scroll_column,
                        padding=10,
                        width=850
                    )
                ],
                scroll=ft.ScrollMode.AUTO

            ),
            actions=[ft.TextButton("Confirm and close", on_click=self.close),
                     ft.TextButton("Cancel and close", on_click=self.cancel)],
            inset_padding=10,  # Убираем стандартные отступы AlertDialog

        )
        self.page.overlay.append(self.dialog)
        self.page.update()

    def collect_values(self, event):
        self.a = None
        self.b = None
        self.n = None
        self.y0 = None
        row_container = self.values_fields.controls[0]
        self.a = float(row_container.content.controls[3].value)
        self.b = float(row_container.content.controls[5].value)
        # self.y0 = float(row_container.content.controls[7].value)
        self.n = int(row_container.content.controls[7].value)
        self.func = self.drp.value
        self.get_data()
        # print('self.a =', self.a, 'self.b = ', self.b, 'n = ', self.n, 'self.func =', self.func)

    def close(self, e):
        self.collect_values(e)
        self.dialog.open = False
        self.page.update()
        self.dialog = None
        self.output.update_text("Data: y = f(x) conditions")
        self.output.update_text(json.dumps(self.page.result, indent=1, ensure_ascii=False))
        self.upd()
        self.page.update()
