import mysql.connector
from voto.voto import Voto

class LibrettoDao:

    def __init__(self):
        pass

    def getAllVoti(self):
        cnx = mysql.connector.connect(user="root",
                                      password="gvpoli",
                                      host="127.0.0.1",
                                      database="libretto")
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM voti"""
        cursor.execute(query)
        result = []
        for row in cursor:
            if row["lode"] == "False":
                result.append(Voto(row["materia"], row["punteggio"], row["data"].date(), False))
            else:
                result.append(Voto(row["materia"], row["punteggio"], row["data"].date(), True))
        cnx.close()
        return result

    def addVoto(self, voto:Voto):
        cnx = mysql.connector.connect(user="root",
                                      password="gvpoli",
                                      host="127.0.0.1",
                                      database="libretto")
        cursor = cnx.cursor()
        query = """INSERT INTO voti (materia, punteggio, data, lode) VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode)))
        cnx.commit() # è un metodo della connessione
        cnx.close()
        return

    def hasVoto(self, voto: Voto):
        cnx = mysql.connector.connect(user="root",
                                      password="gvpoli",
                                      host="127.0.0.1",
                                      database="libretto")
        cursor = cnx.cursor()
        query = """SELECT *
                FROM voti v
                WHERE v.materia = %s"""
        cursor.execute(query, (voto.materia,))
        result = cursor.fetchall()
        return len(result) > 0

if __name__ == "__main__":
    dao = LibrettoDao()
    print(dao.getAllVoti())