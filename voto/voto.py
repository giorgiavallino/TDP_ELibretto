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


class Libretto():

    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti

    def __str__(self):
        stringa = f"Libretto voti di {self.proprietario}\n"
        for voto in self.voti:
            stringa = f"{stringa}{voto}\n"
        return stringa

    def __len__(self):
        return len(self.voti)

    def append(self, voto): # append è un nome più generico che potrebbe essere usato maggiormente rispetto, ad esempio,
        # ad addVoto --> concetto di duck typing
        return self.voti.append(voto)

    def calcoloMedia(self):
        """
        Resistuisce la media dei valori attualmente presenti nel libretto
        :return: valore numerico della media, oppure ValueError se non sono presenti voti nel libretto
        """
        # E' sempre bene commentare i vari moduli e le varie definizioni
        # media = somma dei voti / media degli esami
        if len(self.voti) == 0:
            raise ValueError("Attenzione, la lista esami è vuota!")
        voti = [voto.punteggio for voto in self.voti] # equivalente a fare il ciclo for indentato
        return sum(voti)/len(voti) # si potrebbe anche usare la funzione di Python: math.mean(voti)

    def getVotiByPunti(self, punti, lode):
        """
        restituisce una lista di esami con il punteggio uguale a punti (e lode uguale a lode)
        :param punti: variabile di tipo intero che indica il puntaggio
        :param lode: variabile booleana che indica se è presente la lode
        :return: lista di voti filtrati secondo i parametri
        """
        voti_filtrati = []
        for voto in self.voti:
            if voto.punteggio == punti and voto.lode == lode:
                voti_filtrati.append(voto)
        return voti_filtrati

    def getVotoByName(self, nome):
        """
        restituisce il voto il cui campo materia è uguale a nome
        :param nome: variabile di tipo stringa che indica il nome della materia
        :return: oggetto di tipo Voto oppure None in caso di voto non trovato
        """
        for voto in self.voti:
            if voto.materia == nome:
                return voto


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

