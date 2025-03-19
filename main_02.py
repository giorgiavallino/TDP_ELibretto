# Svolgimento della traccia_01 con l'aggiunta di nuove funzionalità

class Person:

    def __init__(self, nome, cognome, eta, capelli, occhi, casa, incantesimo="Non ancora definito"):
        self.nome = nome
        self._cognome = cognome # la proprietà è più protetta e così pubblica come lo sono le altre proprietà non
        # precedute da un underscore: i livelli di visibilità aumentano nel seguente modo: nessun underscore, un
        # underscore e due underscore
        self.eta = eta
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.__prova = None # proprietà estremamente protetta a cui è più difficile accedere: per stamparla
        # bisognerebbe usare la dicitura oggetto._Person.__prova ma è meglio evitare!
        self.incantesimo = incantesimo

        @property # viene definita una property attraverso cui viene definito un metodo che legge la variabile protetta
        # del cognome
        def cognome(self):
            return self._cognome

        @cognome.setter
        def cognome(self, value):
            self._cognome = value
            return self._cognome

        # @property e @setter vengono utilizzate quando si hanno delle variabili protette che serviranno
        # successivamente nello svolgimento del programma

    def __str__(self):
        return f"Person: {self.nome} {self._cognome} \n"


class Student(Person):

    def __init__(self, nome, cognome, eta, capelli, occhi, casa, animale, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.animale = animale

    def __str__(self):
        return f"Student: {self.nome} {self._cognome} - {self.casa} \n "


class Teacher(Person):

    def __init__(self, nome, cognome, eta, capelli, occhi, casa, materia, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.materia = materia

    def __str__(self):
        return f"Teacher: {self.nome} {self._cognome} - {self.materia}\n"


class Casa:

    def __init__(self, nome, studenti = []):
        self.nome = nome
        self.studenti = studenti

    def addStudente(self, studente):
        self.studenti.append(studente)
        return self.studenti

    def __str__(self):
        if len(self.studenti) == 0:
            return f"La casa {self.nome} è vuota."

        stringa = f"Lista degli studenti iscritti alla casa {self.nome} \n"
        for studente in self.studenti:
            stringa = stringa + str(studente)

        return stringa


class Scuola:

    def __init__(self, case):
        self.case = case

    def __str__(self):
        stringa = ""
        for casa in self.case:
            stringa = stringa + str(casa)
        return stringa


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


# Grifondoro
Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")
Hermione = Student(nome="Hermione", cognome="Granger", eta=11, capelli="castani", occhi="castani", casa="Grifondoro", animale="gatto", incantesimo="Wingardium Leviosa")
Ron = Student(nome="Ron", cognome="Weasley", eta=11, capelli="rossi", occhi="azzurri", casa="Grifondoro", animale="topo")
Neville = Student(nome="Neville", cognome="Paciock", eta=11, capelli="castani", occhi="castani", casa="Grifondoro", animale="rospo")
Ginny = Student(nome="Ginny", cognome="Weasley", eta=10, capelli="rossi", occhi="castani", casa="Grifondoro", animale="gatto")
Sirius = Person(nome="Sirius", cognome="Black", eta=36, capelli="neri", occhi="grigi", casa="Grifondoro") #Sirius non è ne studente ne professore ad Hogwarts
Remus = Teacher(nome="Remus", cognome="Lupin", eta=36, capelli="castani", occhi="verdi", casa="Grifondoro", materia="Difesa contro le arti oscure")
Minerva = Teacher(nome="Minerva", cognome="McGranitt", eta=70, capelli="neri", occhi="verdi", casa="Grifondoro", materia="Trasfigurazione", incantesimo="Trasfigurazione Animale")
Albus = Teacher(nome="Albus", cognome="Silente", eta=115, capelli="argento", occhi="azzurri", casa="Grifondoro", materia="Preside")
Rubeus = Person(nome="Rubeus", cognome="Hagrid", eta=60, capelli="neri", occhi="neri", casa="Grifondoro") #Rubeus non è ne studente ne professore ad Hogwarts
James = Person(nome="James", cognome="Potter", eta=23, capelli="neri", occhi="castani", casa="Grifondoro")
Lily = Person(nome="Lily", cognome="Evans", eta=23, capelli="rosso", occhi="verdi", casa="Grifondoro")
Fred = Student(nome = "Fred", cognome = "Weasley", eta = 16, capelli = "rossi", occhi = "castani", casa = "Grifondoro", animale="nessuno")
George = Student(nome = "George", cognome = "Weasley", eta = 16, capelli = "rossi", occhi = "castani", casa = "Grifondoro", animale="nessuno")

# Serpeverde
Draco = Student(nome="Draco", cognome="Malfoy", eta=11, capelli="biondi", occhi="grigi", casa="Serpeverde", animale="nessuno")
Severus = Teacher(nome="Severus", cognome="Snape", eta=45, capelli="neri", occhi="neri", casa="Serpeverde", materia="Pozioni", incantesimo="Sectumsempra")
Horace = Teacher(nome="Horace", cognome="Lumacorno", eta=65, capelli="brizzolati", occhi="verdi", casa="Serpeverde", materia="Pozioni", )
Bellatrix = Person(nome="Bellatrix", cognome="Lestrange", eta=47, capelli="neri", occhi="neri", casa="Serpeverde") #Bellatrix non è ne studente ne professore ad Hogwarts
Lucius = Person(nome="Lucius", cognome="Malfoy", eta=42, capelli="biondi", occhi="grigi", casa="Serpeverde") #Lucius non è ne studente ne professore ad Hogwarts
Narcissa = Person(nome="Narcissa", cognome="Malfoy", eta=41, capelli="biondi", occhi="azzurri", casa="Serpeverde") #Narcissa non è ne studente ne professore ad Hogwarts
Pansy = Student(nome="Pansy", cognome="Parkinson", eta=12, capelli="neri", occhi="castani", casa="Serpeverde", animale="nessuno")
Blaise = Student(nome = "Blaise", cognome = "Zabini", eta = 12, capelli = "neri", occhi = "castani", casa = "Serpeverde", animale="nessuno")
Tom_Riddle = Student(nome="Tom", cognome="Riddle", eta=16, capelli="neri", occhi="neri", casa="Serpeverde", animale="serpente", incantesimo="Avada Kedavra")

# Corvonero
Luna = Student(nome="Luna", cognome="Lovegood", eta=11, capelli="biondi", occhi="azzurri", casa="Corvonero", animale="nessuno")
Cho = Student(nome="Cho", cognome="Chang", eta=12, capelli="neri", occhi="castani", casa="Corvonero", animale="nessuno")
Gilderoy = Teacher(nome="Gilderoy", cognome="Allock", eta=33, capelli="biondi", occhi="azzurri", casa="Corvonero", materia="Difesa contro le Arti Oscure", incantesimo="Oblivion")
Filius = Teacher(nome="Filius", cognome="Vitious", eta=150, capelli="bianchi", occhi="azzurri", casa="Corvonero", materia="Incantesimi", incantesimo="Wingardium Leviosa")
Xenophilius = Person(nome="Xenophilius", cognome="Lovegood", eta=49, capelli="bianchi", occhi="azzurri", casa="Corvonero") #Xenophilius non è ne studente ne professore ad Hogwarts
Padma = Student(nome="Padma", cognome="Patil", eta=13, capelli="neri", occhi="castani", casa="Corvonero", animale="nessuno")
Michael = Student(nome = "Michael", cognome = "Corner", eta = 13, capelli = "neri", occhi = "castani", casa = "Corvonero", animale="nessuno")

# Tassorosso
Cedric = Student(nome="Cedric", cognome="Diggory", eta=16, capelli="castani", occhi="grigi", casa="Tassorosso", animale="nessuno")
Pomona = Teacher(nome="Pomona", cognome="Sprout", eta=60, capelli="grigi", occhi="castani", casa="Tassorosso", materia="Erbologia")
Hannah = Student(nome="Hannah", cognome="Abbott", eta=12, capelli="biondi", occhi="azzurri", casa="Tassorosso", animale="nessuno")
Ernest = Student(nome="Ernest", cognome="Macmillan", eta=13, capelli="biondi", occhi="castani", casa="Tassorosso", animale="nessuno")
Susan = Student(nome="Susan", cognome=" Bones", eta=12, capelli="rossi", occhi="verdi", casa="Tassorosso", animale="nessuno")
Ted = Person(nome="Ted", cognome="Tonks", eta=24, capelli="castano", occhi="neri", casa="Tassorosso") #Ted non è ne studente ne professore ad Hogwarts

print(Harry, Ron, Susan, Xenophilius, Remus)

personaggi = [Harry, Hermione, Ron, Neville, Ginny, Sirius, Remus, Minerva, Albus, Rubeus, James, Lily, Fred, George,
              Draco, Severus, Horace, Bellatrix, Lucius, Narcissa, Pansy, Blaise, Luna, Cho, Gilderoy, Filius, Xenophilius,
              Padma, Michael, Cedric, Pomona, Hannah, Ernest, Susan, Ted]


grifondoro = Casa("Grifondoro")
tassorosso = Casa("Tassorosso")
corvonero = Casa("Corvonero")
serpeverde = Casa("Serpeverde")

for p in personaggi:
    # if p.casa == grifondoro.nome & isinstance(p, Student):
    #     grifondoro.addStudente(p)
    # if p.casa == tassorosso.nome & isinstance(p, Student):
    #     tassorosso.addStudente(p)
    # if p.casa == corvonero.nome & isinstance(p, Student):
    #     corvonero.addStudente(p)
    # if p.casa == serpeverde.nome & isinstance(p, Student):
    #     serpeverde.addStudente(p)
    if isinstance(p,Student):
        match p.casa: # è un metodo alternativo al ciclo if per cercare i match
            case "Grifondoro":
                grifondoro.addStudente(p)
            case "Tassorosso":
                tassorosso.addStudente(p)
            case "Corvonero":
                corvonero.addStudente(p)
            case "Serpeverde":
                serpeverde.addStudente(p)
            case _:
                print(f"Jumping {p}")

print(grifondoro)


v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
v2 = Voto("Pozioni", 30, "2022-02-17", True)
v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)

libretto = Libretto(Harry, [v1, v2])
print(libretto)
libretto.append(v3)
print(libretto)