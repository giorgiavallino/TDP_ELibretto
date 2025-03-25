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

    def copy(self):
        return Student(self.nome, self._cognome, self.eta, self.capelli, self.occhi, self.casa, self.animale,
                       self.incantesimo)


class Teacher(Person):

    def __init__(self, nome, cognome, eta, capelli, occhi, casa, materia, incantesimo="Non ancora definito"):
        super().__init__(nome, cognome, eta, capelli, occhi, casa, incantesimo)
        self.materia = materia

    def __str__(self):
        return f"Teacher: {self.nome} {self._cognome} - {self.materia}\n"