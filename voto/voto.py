class Voto:

    def __init__(self, materia, punteggio, data, lode):
        if punteggio == 30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = lode # potrebbe riferirsi a un valore booleano
        elif punteggio <30:
            self.materia = materia
            self.punteggio = punteggio
            self.data = data
            self.lode = False
        else:
            raise ValueError(f"Attenzione: non è possibile creare un voto con un punteggio {punteggio}")

    def __str__(self):
        if self.lode:
            return f"In {self.materia} hai preso {self.punteggio} e lode il {self.data}"
        else:
            return f"In {self.materia} hai preso {self.punteggio} il {self.data}"

class Libretto():

    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def append(self, voto): # append è un nome più generico che potrebbe essere usato maggiormente rispetto, ad esempio,
        # ad addVoto --> concetto di duck typing
        return self.voti.append(voto)

    def __str__(self):
        stringa = f"Libretto voti di {self.proprietario}\n"
        for voto in self.voti:
            stringa = f"{stringa}{voto}\n"
        return stringa

def testVoto():

    v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
    v2 = Voto("Pozioni", 30, "2022-02-17", True)
    v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)

    libretto = Libretto("Harry", [v1, v2])
    print(libretto)
    libretto.append(v3)
    print(libretto)

if __name__ == "__main__": # in questo modo quando viene importato il modulo voto, tutto il codice scritto sotto e
    # sopra nella funzione testVoto non viene stampato ed eseguito
    testVoto()

