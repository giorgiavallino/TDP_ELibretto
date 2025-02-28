# Svolgimento della traccia con l'aggiunta di nuove funzionalità

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