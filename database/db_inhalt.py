import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("meine_datenbank.db")
        self.c = self.conn.cursor()
        self.engine = create_engine("sqlite:///meine_datenbank.db")
        self.Session = sessionmaker(bind=self.engine)

    def anzeigen_tankvorgaenge_inhalt(self):
        self.c.execute("SELECT datum, liter, preis, gefahrene_km FROM tankvorgaenge")
        results = self.c.fetchall()

        for row in results:
            print("Datum:", row[0])
            print("Liter:", row[1])
            print("Preis:", row[2])
            print("Gefahrene Kilometer:", row[3])
            print()  # Leerzeile zur besseren Lesbarkeit

    def close_connection(self):
        self.conn.close()


db = Database()
db.anzeigen_tankvorgaenge_inhalt()
db.close_connection()
