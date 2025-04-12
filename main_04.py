import flet as ft
from UI.controller import Controller
from UI.view import View

# Viene aggiunto il codice per creare l'interfaccia grafica (confrontare con controller e view)

def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.setController(c)
    v.loadInterface()

ft.app(target=main)