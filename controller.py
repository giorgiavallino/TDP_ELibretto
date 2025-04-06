from view import View

class Controller:

    def __init__(self, view: View):
        self._view = view

    def handleAggiungi(self, e):
        strIn = self._view._txtIn.value
        if strIn == "":
            self._view._txtOut.value = "Errore: campo vuoto!"
            self._view._page.update()
            return
        self._view._txtOut.value = strIn
        self._view._page.update()