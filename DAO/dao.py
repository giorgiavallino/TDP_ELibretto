from voto.voto import Voto
from DAO.dbConnect import DBConnect

class LibrettoDao:

    def __init__(self): # metodo standard che ha accesso a self
        pass

    @staticmethod # --> non accede ai parametri della classe, ma semplicemente hai parametri che vengono passati al suo
    # interno
    def getAllVoti():
        cnx = DBConnect.getConnectionPool()
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

    @staticmethod
    def addVoto(voto:Voto):
        cnx = DBConnect.getConnectionPool()
        cursor = cnx.cursor()
        query = """INSERT INTO voti (materia, punteggio, data, lode) VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (voto.materia, voto.punteggio, voto.data, str(voto.lode)))
        cnx.commit() # è un metodo della connessione
        cnx.close()
        return

    @staticmethod
    def hasVoto(voto: Voto):
        cnx = DBConnect.getConnectionPool()
        cursor = cnx.cursor()
        query = """SELECT *
                FROM voti v
                WHERE v.materia = %s"""
        cursor.execute(query, (voto.materia,))
        result = cursor.fetchall()
        cnx.close()
        return len(result) > 0


if __name__ == "__main__":
    dao = LibrettoDao()
    print(dao.getAllVoti())