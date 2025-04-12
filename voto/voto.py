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

    def __repr__(self):
        return f"{self.materia}: {self.punteggio}, {self.lode}, {self.data}"

    def __hash__(self):
        return hash(self.materia)

    def __eq__(self, other):
        return self.materia == other.materia # due oggetti sono uguali se hanno la stessa materia

    def copy(self):
        return Voto(self.materia, self.punteggio, self.data, self.lode)