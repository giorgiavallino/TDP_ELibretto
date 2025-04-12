import datetime

import flet as ft

class View:

    def __init__(self, page: ft.Page):
        self._page = page
        self._controller = None

    def setController(self, controller):
        self._controller = controller

    def _fillDDVoto(self):
        for i in range(18,30):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append(ft.dropdown.Option("30L"))

    def loadInterface(self):
        """
        vengono definiti e caricati tutti i controlli dell'interfaccia
        :return:
        """
        self._page.bgcolor = "white"

        self._titolo = ft.Text(value="Libretto Voti",
                               color="red", size=24)
        self._student = ft.Text(value=self._controller.getStudent(),
                                color="brown")

        row_01 = ft.Row([self._titolo],
                        alignment=ft.MainAxisAlignment.CENTER)
        row_02 = ft.Row([self._student],
                        alignment=ft.MainAxisAlignment.END)

        self._txtInNome = ft.TextField(label="Nome esame",
                                       hint_text="Inserisci il nome dell'esame",
                                       width=300)
        self._ddVoto = ft.Dropdown(label="Voto",
                                   width=120)
        self._fillDDVoto()
        self._dp = ft.DatePicker(first_date=datetime.datetime(2022, 1, 1),
                                 last_date=datetime.datetime(2026, 12, 31),
                                 on_change=lambda _: print(f"Giorno selezionato {self._dp.value}"),
                                 on_dismiss=lambda _: print(f"Data non selezionata!"))
        self._btnCal = ft.ElevatedButton(text="Pick date",
                                         icon=ft.Icons.CALENDAR_MONTH,
                                         on_click=lambda _:self._page.open(self._dp))
        self._btnAdd = ft.ElevatedButton(text="Aggiungi",
                                         on_click=self._controller.handleAggiungi)
        self._btnPrint = ft.ElevatedButton(text="Stampa",
                                           on_click=self._controller.handleStampa)

        row_03 = ft.Row([self._txtInNome, self._ddVoto, self._btnCal, self._btnAdd, self._btnPrint],
                        alignment=ft.MainAxisAlignment.CENTER)

        self._txtOut = ft.ListView(expand=True)

        row_04 = ft.Row([self._txtOut])

        self._page.add(row_01, row_02, row_03, row_04)