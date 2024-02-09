import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.tankvorgang import Tankvorgang^4

class Database:
    def __init__(self):
        # SQLite-Datenbankverbindung initialisieren
        self.conn = sqlite3.connect("meine_datenbank.db")
        self.c = self.conn.cursor()

        # SQLAlchemy-Engine und Sessionmaker initialisieren
        self.engine = create_engine("sqlite:///meine_datenbank.db")
        self.Session = sessionmaker(bind=self.engine)

    def anzeigen_tankvorgaenge_inhalt(self):
        # Abfrage zum Abrufen aller Datensätze aus der Tabelle "tankvorgaenge"
        self.c.execute("SELECT * FROM tankvorgaenge")
        results = self.c.fetchall()

        # Beispiel für die Anzeige der Ergebnisse
        for row in results:
            print("ID:", row[0])
            print("Auto ID:", row[1])
            print("Datum:", row[2])
            print("Liter:", row[3])
            print("Preis pro Liter:", row[4])
            print("Gefahrene Kilometer:", row[5])
            print()  # Leerzeile zur besseren Lesbarkeit

    def close_connection(self):
        # Verbindung zur Datenbank schließen
        self.conn.close()


# Beispiel für die Verwendung der Database-Klasse
db = Database()
db.anzeigen_tankvorgaenge_inhalt()
db.close_connection()
