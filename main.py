import flet as ft 
import Credits as cr
import Masuma
# import Rossko

def main(page: ft.Page):
    page.title = "Flet App"

# Rossko.parser("32421")
Masuma.parser()
ft.app(target=main)