import flet as ft
import Credits as cr
import Masuma

def main(page: ft.Page):
    page.title = "Flet App"

Masuma.parser()
ft.app(target=main)