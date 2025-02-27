# Svolgimento della traccia

# Si potrebbero utilizzare delle liste: ogni persona è rappresentata da un lista eterogenea con i vari parametri
# richiesti
# Utilizzare questa struttura non è ottimale: bisogna ricordarsi a quale parametro corrisponde ciascun campo,...

# Per rendere più efficiente questo meccanismo dal momento che le proprietà di ciascuna persona si ripetono invariate,
# è preferibile utilizzare una classe:

class Person: #istanziare una classe

    def __init__(self, nome, cognome, age, capelli, occhi, casa, incantesimo = "Non ancora definito"): # definire il
        # costruttore
        self.nome = nome
        self.cognome = cognome
        self.age = age
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.incantesimo = incantesimo

    def __str__(self): # metodo che permette di stampare l'oggetto
        return f"{self.nome} {self.cognome} \n"


class Student(Person): # viene creata una classe Student che eredita dalla classe Persona... anche i metodi di Persona
    # vengono ereditati, ma possono eventualmente essere riscritti nella classe Student

    def __init__(self, nome, cognome, age, capelli, occhi, casa, animale, incantesimo = "Non ancora definito"):
        super().__init__(nome, cognome, age, capelli, occhi, casa, incantesimo) # usare super() equivale a Persona():
        # evita di inizializzare nuovamente le variabili di Persona, ma le eredita da questa classe attraverso il
        # richiamo del suo __init__
        self.animale = animale

    def __str__(self): # viene riscritta la funzione __str__ della classe Persona
        return f"{self.nome} {self.cognome} - {self.casa} \n"

    #def __repr__(self): # ha una funzione analoga a __str__: __str__ viene usata per avere una stampa carina, invece
    # __repr__ viene usata dal programmatore per visualizzare come è un oggetto
        #return (f"Student: {self.nome}, {self.cognome}, {self.age} {self.capelli}, {self.occhi}, {self.casa}, "
                #f"{self.animale}, {self.incantesimo}")


class Teacher(Person):

    def __init__(self, nome, cognome, age, capelli, occhi, casa, materia, incantesimo = "Non ancora definito"):
        super().__init__(nome, cognome, age, capelli, occhi, casa, incantesimo)
        self.materia = materia

    def __str__(self):
        return f"Teacher: {self.nome} {self.cognome} - {self.casa} \n"


class Casa:

    def __init__(self, nome, studenti = []):
        self.nome = nome
        self.studenti = studenti

    def addStudente(self, studente):
        self.studenti.append(studente) # append aggiunge un solo elemento, extend, se si passa una lista, li aggiunge
        # tutti come singoli elementi
        return self.studenti

    def __str__(self):

        if len(self.studenti) == 0:
            return "La casa {self.nome} è vuota."

        mystr =  f"\nLista degli studenti iscritti alla casa {self.nome}: \n"
        for s in self.studenti:
            mystr = mystr + str(s)

        return mystr


Harry = Person("Harry", "Potter", 11, "castani", "azzurri", "Grifondoro") # avendo
# definito un incantesimo di default all'interno del metodo __init__, si può non inserire negli attributi dell'oggetto:
# facendo così, l'incantesimo corrisponderà a quello scelto di default nell'__init__

Ron = Student("Ron", "Weasley", 11, "rossi", "castani", "Grifondoro",
              "topo")

Severus = Teacher("Severus", "Snape", 45, "neri", "neri", "Serpeverde",
                  "Pozioni", "Sectumsempra")


print(Harry)
print(Ron)
print(Severus)


Grifondoro = Casa("Grifondoro", [Harry])
print(Grifondoro)
Grifondoro.addStudente(Ron)
print(Grifondoro)
