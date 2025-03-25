from scuola import Student
from voto.voto import Libretto, Voto

Harry = Student(nome="Harry", cognome="Potter", eta=11, capelli="castani", occhi="azzurri", casa="Grifondoro", animale="civetta", incantesimo="Expecto Patronum")

mylib = Libretto(Harry, [])

v1 = Voto("Trasfigurazione", 25, "2022-02-13", False)
v2 = Voto("Pozioni", 25, "2022-02-17", True)

mylib.append(v1)
mylib.append(v2)

mylib.append(Voto("Difesa contro le arti oscure", 27, "2022-04-13", False))

print(mylib.calcoloMedia())

voti_filtrati = mylib.getVotiByPunti(25, False)
print(voti_filtrati)

voto_trasfigurazione = mylib.getVotoByName("Trasfigurazione")
print(voto_trasfigurazione)

print("Verifica aggiunta")
print(mylib.hasVoto(v1))
print(mylib.hasVoto(Voto("Aritmanzia", 30, "2023-07-10", False)))
print(mylib.hasVoto(Voto("Difesa contro le arti oscure", 27, "2022-04-13", False)))

print("Verifica conflitto")
print(mylib.hasConflitto(Voto("Difesa contro le arti oscure", 21, "2022-04-13", False)))

mylib.append(Voto("Aritmanzia", 30, "2023-07-10", False))
#mylib.append(Voto("Difesa contro le arti oscure", 27, "2022-04-13", False))

mylib.append(Voto("Divinazione", 27, "2021-02-03", False))
mylib.append(Voto("Cura delle creature magiche", 26, "2021-06-14", False))

print("Libretto originario")
print(mylib)
print("Libretto migliorato")
print(mylib.creaMigliorato())

print("Libretto ordinato per materia")
print(mylib.creaLibOrdinatoPerMateria())

print("Libretto ordinato per voto")
print(mylib.creaLibOrdinatoPerVoto())

print("Libretto con cancellazione dei voti inferiori al punteggio inserito")
lib_ordinato = mylib.creaLibOrdinatoPerVoto()
lib_ordinato.cancellaInferiori(24)
print(lib_ordinato)