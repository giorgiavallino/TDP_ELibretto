import flet as ft

class View:

    def __init__(self, page: ft.Page):
        self._page = page
        self._controller = None

    def setController(self, controller):
        self._controller = controller

    def loadInterface(self):
        """
        vengono definiti e caricati tutti i controlli dell'interfaccia
        :return:
        """
        self._txtIn = ft.TextField(label="Inserisci nome")
        self._btnIn = ft.ElevatedButton(text="Aggiungi",
                                  on_click = self._controller.handleAggiungi)
        row = ft.Row([self._txtIn, self._btnIn])
        self._txtOut = ft.Text("")
        self._page.add(row, self._txtOut)