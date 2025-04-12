import mysql.connector

class DBConnect:

    @classmethod # è un metodo di classe --> significa che questa classe è unica --> centralizza la creazione
    # di connessioni
    def getConnection(self):
        try:
            cnx = mysql.connector.connect(user="root",
                                      password="gvpoli",
                                      host="127.0.0.1",
                                      database="libretto")
            return cnx
        except mysql.connector.Error as err:
            print("Non è stata creata nessuna connessione:")
            print(err)
            return None