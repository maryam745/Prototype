import flet as ft
from helper import *
class Login_View(ft.View):
    def __init__(self, page):
        super().__init__(route="/")
        self.page = page  # Store reference to the main page
        # Layout
        self.controls = [ft.AppBar(
        title=ft.Text("Maryam"),
        center_title=False,  # Centers the title
        bgcolor=ft.colors.PINK,  # Optional background color
    ),
            ft.Text(value='Welcome to login page',font_family="Arial",color=ft.colors.BLUE_GREY_700),
            ft.OutlinedButton(text='next',icon=ft.Icons.ARROW_FORWARD_IOS,on_click= lambda _: self.page.go("/sign_up"))
        ]
        self.horizontal_alignment = "center"
        self.padding = 25
        self.vertical_alignment = "center" 