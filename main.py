# Svolgimento della traccia

# Si potrebbero utilizzare delle liste: ogni persona è rappresentata da un lista eterogenea con i vari parametri
# richiesti
# Utilizzare questa struttura non è ottimale: bisogna ricordarsi a quale parametro corrisponde ciascun campo,...

# Per rendere più efficiente questo meccanismo dal momento che le proprietà di ciascuna persona si ripetono invariate,
# è preferibile utilizzare una classe:

class Persona: #istanziare una classe

    def __init__(self, nome, cognome, age, capelli, occhi, casa, incantesimo): #definire il costruttore
        self.nome = nome
        self.cognome = cognome
        self.age = age
        self.capelli = capelli
        self.occhi = occhi
        self.casa = casa
        self.incantesimo = incantesimo #1:50