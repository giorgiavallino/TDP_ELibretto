import mysql.connector

class DBConnect:

    def __init__(self):
        RuntimeError("Non creare una istanza di questa classe per favore!")

    _myPool = None

    @classmethod # è un metodo di classe --> significa che questa classe è unica --> centralizza la creazione
    # di connessioni
    def getConnection(cls):
        try:
            cnx = mysql.connector.connect(user="root",
                                      password="gvpoli",
                                      host="127.0.0.1",
                                      database="libretto") # si può inizializzare un file contenente queste informazioni
            return cnx
        except mysql.connector.Error as err:
            print("Non è stata creata nessuna connessione:")
            print(err)
            return None

    # Viene introdotto il pooling:
    @classmethod
    def getConnectionPool(cls):
        if cls._myPool is None:
            try:
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(user="root",
                                                                      password="gvpoli",
                                                                      host="127.0.0.1",
                                                                      database="libretto",
                                                                      pool_size=3,
                                                                      pool_name="myPool")
            except mysql.connector.Error as err:
                print("Something is wrong in DBConnect:")
                print(err)
                return None
            return cls._myPool.get_connection()
        # = se il Pool non esiste, viene creata una connessione e viene restituito il metodo get_connection()
        else:
            return cls._myPool.get_connection()
        # = se il Pool esiste già, allora viene restituita direttamente la connessione tramite il metodo
        # get_connection()