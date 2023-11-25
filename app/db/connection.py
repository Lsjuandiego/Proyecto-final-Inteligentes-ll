from pymongo import MongoClient
import configparser


class MongoConnection:
    def __init__(self):
        """
        Inicializa la clase MongoConnection y lee la configuración desde
        config.ini.
        """
        self.config = configparser.ConfigParser()
        self.config.read('./app/db/config.ini')
        self.user = self.config.get('DATABASE', 'DB_USER')
        self.password = self.config.get('DATABASE', 'DB_PASS')
        self.db = self.config.get('DATABASE', 'DB_CLUSTER')

    def get_mongo_connection(self):
        """
        Obtiene una conexión a la base de datos MLearning.

        Returns:
            pymongo.database.Database: La conexión a la base de datos MLearning.
        """
        try:
            client = MongoClient('mongodb+srv://' + self.user + ':' + self.password +
                                 '@' + self.db + '.bb9vjrc.mongodb.net/?retryWrites=true&w=majority')
            return client['MLearning']
        except Exception as e:
            print("Error connecting to MongoDB:", e)
            return None

    def close_connection(self, client):
        """
        Cierra la conexión a la base de datos MongoDB.

        Args:
            client (pymongo.MongoClient): El cliente de MongoDB a cerrar.
        """
        try:
            client.close()
            print("MongoDB connection closed.")
        except Exception as e:
            print("Error closing MongoDB connection:", e)
