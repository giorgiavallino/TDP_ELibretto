import operator
from voto.voto import Voto
from DAO.dao import LibrettoDao

# Questo file rappresenta il modello

class Libretto:

    def __init__(self, proprietario, voti = []):
        self.proprietario = proprietario
        self.voti = voti
        self.dao = LibrettoDao()
        self._fillLibretto()

    def __str__(self):
        stringa = f"Libretto voti di {self.proprietario}\n"
        for voto in self.voti:
            stringa = f"{stringa}{voto}\n"
        return stringa

    def __len__(self):
        return len(self.voti)

    def __eq__(self, other):
        return (self.materia == other.materia and self.punteggio == other.punteggio and self.lode == other.lode)
    # si potrebbe usare al posto del metodo hasVoto, ma risulta meno elegante... quindi, è preferibile l'altro meotodo

    def append(self, voto): # append è un nome più generico che potrebbe essere usato maggiormente rispetto, ad esempio,
        # ad addVoto --> concetto di duck typing
        if (self.hasConflitto(voto) is False and self.hasVoto(voto) is False):
            self.voti.append(voto)
            if not self.dao.hasVoto(voto):
                self.dao.addVoto(voto)
        else:
            raise ValueError("Il voto è già presente")

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
        :param punti: variabile di tipo intero che indica il punteggio
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

    def hasVoto(self, voto):
        """
        verifica se il libretto contiene già il voto: due voti vengono considerati uguali se hanno lo stesso campo
        materia e lo stesso voto (costituito da punteggio e lode che dovranno, quindi, essere uguali)
        :param voto: istanza dell'oggetto di tipo Voto
        :return: bool --> true se il voto è già presente nel libretto, false altrimenti
        """
        for v in self.voti:
            if (v.materia == voto.materia and v.punteggio == voto.punteggio and v.lode == voto.lode):
                return True
        return False

    def hasConflitto(self, voto):
        """
        controlla che il Voto voto non presenti un conflitto con i voti già presenti nel libretto: due voti sono in
        conflitto quando hanno lo stesso campo materia, ma diversa coppia (punteggio, lode)
        :param voto: istanza dell'oggetto di tipo Voto
        :return: bool --> true se il voto è in conflitto, altrimenti false
        """
        for v in self.voti:
            if (v.materia == voto.materia and not (v.punteggio == voto.punteggio and v.lode == voto.lode)):
                return True
        return False

    def copy(self):
        """
        crea una nuova copia del libretto
        :return: istanza della classe Libretto
        """
        nuovo_libretto = Libretto(self.proprietario, [])
        for v in self.voti:
            nuovo_libretto.append(v.copy())
        return nuovo_libretto

    def creaMigliorato(self):
        """
        crea un nuovo oggetto Libretto in cui i voti sono migliorati secondo la seguente logica:
        - se il voto è >= 18 e < 24, viene aggiunto + 1
        - se il voto è >= 24 e < 29, viene aggiunto + 2
        - se il voto è 29, viene aggiunto + 1
        - se il voto è 30, rimane 30
        :return: nuovo libretto
        """
        nuovo_libretto = self.copy()
        for voto in nuovo_libretto.voti:
            if 18 <= voto.punteggio < 24:
                voto.punteggio = voto.punteggio + 1
            elif 24 <= voto.punteggio < 29:
                voto.punteggio = voto.punteggio + 2
            elif voto.punteggio == 29:
                voto.punteggio = 30
        return nuovo_libretto

    def sortByMateria(self):
        #self.voti.sort(key=estraiMateria) # key deve essere uguale a una funzione esterna alle classi (che indica il
        # criterio dell'ordinamento)
        # al posto di usare sort, si può usare attrgetter:
        self.voti.sort(key=operator.attrgetter("materia"))

    def creaLibOrdinatoPerVoto(self):
        """
        crea un nuovo oggetto Libretto e lo ordina per voto
        :return: nuovo istanza dell'oggetto Libretto
        """
        nuovo_libretto = self.copy()
        nuovo_libretto.voti.sort(key=lambda v:(v.punteggio, v.lode), reverse=True)
        return nuovo_libretto

    def creaLibOrdinatoPerMateria(self):
        """
        crea un nuovo oggetto Libretto e lo ordina per materia
        :return: nuova istanza dell'oggetto Libretto
        """
        nuovo_libretto = self.copy()
        nuovo_libretto.sortByMateria()
        return nuovo_libretto

    def cancellaInferiori(self, punteggio):
        """
        agisce sul libretto corrente eliminando tutti i voti inferiori al punteggio inserito
        :param punteggio: intero indicante il valore sotto il quale devo essere eliminati i voti presenti nel libretto
        :return:
        """
        nuovo = []
        for v in self.voti:
            if v.punteggio >= punteggio:
                nuovo.append(v)
        self.voti = nuovo

    def _fillLibretto(self):
        esami = self.dao.getAllVoti()
        for esame in esami:
            self.append(esame)

def estraiMateria(voto):
    """
    questo metodo restituisce il campo materia dell'oggetto voto
    :param voto: istanza della classe Voto
    :return: stringa rappresentante il nome della materia
    """
    return voto.materia

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

