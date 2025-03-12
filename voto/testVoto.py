from voto.voto import Voto, Libretto

v1 = Voto("Trasfigurazione", 24, "2022-02-13", False)
v2 = Voto("Pozioni", 30, "2022-02-17", True)
v3 = Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)

libretto = Libretto("Harry", [v1, v2])
print(libretto)
libretto.append(v3)
print(libretto)

# In questo file vengono eseguiti dei test riferiti al file voto per verificare la correttezza del codice scritto in
# tale file: questo può essere fatto anche nel file voto! (vedere file voto.py)