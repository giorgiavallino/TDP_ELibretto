from view import View
from scuola import Student
from voto.voto import Libretto
from voto.voto import Voto
import flet as ft

class Controller:

    def __init__(self, view: View):
        self._view = view
        self._student = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri",
                                casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
        self._model = Libretto(self._student)
        self._fillLibretto()

    def _fillLibretto(self):
        v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
        v2 = Voto("Pozioni", 30, "2022-02-17", True)
        v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)
        self._model.append(v1)
        self._model.append(v2)
        self._model.append(v3)

    def getStudent(self):
        """
        restituisce informazioni sullo studente
        :return:
        """
        return str(self._student)

    def handleAggiungi(self, e):
        # Cosa fa?
        # 1. Raccoglie tutte le informazioni per creare un nuovo voto
        # 2. Crea un oggetto Voto (con queste informazioni)
        # 3. Fa append sul libretto
        nome = self._view._txtInNome.value
        if nome == "":
            self._view._txtOut.controls.append(ft.Text("Attenzione: il campo nome non può essere vuoto!",
                                                       color="red"))
            self._view._page.update()
            return # in questo caso non ha senso proseguire
        punteggio = self._view._ddVoto.value
        if punteggio is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione: bisogna selezionare un voto!",
                                                       color="red"))
            self._view._page.update()
            return
        data = self._view._dp.value
        if data is None:
            self._view._txtOut.controls.append(ft.Text("Attenzione: bisogna selezionare una data!",
                                                       color="red"))
            self._view._page.update()
            return
        if punteggio == "30L":
            self._model.append(Voto(nome, 30, f"{data.year}-{data.month}-{data.day}", True))
        else:
            self._model.append(Voto(nome, int(punteggio), f"{data.year}-{data.month}-{data.day}", False))
        self._view._txtOut.controls.append(ft.Text("Voto correnttamente aggiunto!",
                                                   color="green"))
        self._view._page.update()


    def handleStampa(self, e):
         self._view._txtOut.controls.append(ft.Text(str(self._model)))
         self._view._page.update()