import sqlite3
from tkinter import messagebox
from datetime import datetime


class TankvorgaengeController:
    def __init__(self, view, datum_entry, liter_entry, preis_entry, km_entry):
        self.view = view
        self.datum_entry = datum_entry
        self.liter_entry = liter_entry
        self.preis_entry = preis_entry
        self.km_entry = km_entry

    def speichern(self):
        datum = self.datum_entry.get()
        liter = self.liter_entry.get()
        preis = self.preis_entry.get()
        km = self.km_entry.get()

        try:
            # Überprüfen des Datumsformats
            datetime.strptime(datum, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Fehler", "Ungültiges Datumsformat")
            return

        # Konvertieren der Eingaben in Float mit flexiblerem Dezimaltrennzeichen
        liter = self.convert_to_float(liter)
        preis = self.convert_to_float(preis)
        km = self.convert_to_float(km)

        # Überprüfen, ob die Konvertierung erfolgreich war
        if liter is None or preis is None or km is None:
            messagebox.showerror("Fehler", "Ungültige numerische Eingabe")
            return

        try:
            # Verbindung zur SQLite-Datenbank herstellen
            conn = sqlite3.connect("meine_datenbank.db")
            c = conn.cursor()

            # Tabelle erstellen (falls nicht vorhanden)
            c.execute(
                """CREATE TABLE IF NOT EXISTS tankvorgaenge
                    (datum TEXT, liter FLOAT, preis FLOAT, km FLOAT)"""
            )

            # Daten einfügen
            c.execute(
                "INSERT INTO tankvorgaenge (datum, liter, preis, km) VALUES (?, ?, ?, ?)",
                (datum, liter, preis, km),
            )

            # Änderungen bestätigen
            conn.commit()
            messagebox.showinfo("Gespeichert", "Tankvorgang gespeichert")

        except sqlite3.Error as e:
            # Fehlerbehandlung bei Datenbankfehlern
            messagebox.showerror("Fehler", "Datenbankfehler: " + str(e))

        finally:
            # Verbindung schließen
            conn.close()

    def convert_to_float(self, entry_text):
        # Ersetzen von ',' durch '.', falls vorhanden
        entry_text = entry_text.replace(",", ".")
        try:
            # Versuche den Text in eine Gleitkommazahl umzuwandeln
            float_value = float(entry_text)
            return float_value
        except ValueError:
            # Wenn die Umwandlung fehlschlägt, gebe None zurück
            return None
