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
