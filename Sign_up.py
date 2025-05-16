import flet as ft
from helper import *
class Sigup_View(ft.View):
    def __init__(self, page):
        super().__init__(route="/sign_up")
        self.page = page  # Store reference to the main page
        # Layout
        self.controls = [
            ft.Text(value='Sign up page',
                    weight=50,color=ft.colors.GREEN,),
            ft.OutlinedButton(text='Previous',icon=ft.Icons.ARROW_BACK,on_click= lambda _: self.page.go("/"))
        ]
        self.horizontal_alignment = "center"
        self.padding = 25
        self.vertical_alignment = "center" 