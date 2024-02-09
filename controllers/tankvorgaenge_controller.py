from tkinter import messagebox
import sqlite3
import datetime


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
            datetime.datetime.strptime(datum, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Fehler", "Ungültiges Datumsformat")
            return

        try:
            liter = float(liter)
            preis = float(preis)
            km = float(km)
        except ValueError:
            messagebox.showerror("Fehler", "Ungültige numerische Eingabe")
            return

        self.conn = sqlite3.connect("meine_datenbank.db")
        try:
            c = self.conn.cursor()
            c.execute(
                """CREATE TABLE IF NOT EXISTS tankvorgaenge
                    (datum TEXT, liter FLOAT, preis FLOAT, km FLOAT)"""
            )
            c.execute(
                "INSERT INTO tankvorgaenge (datum, liter, preis, km) VALUES (?, ?, ?, ?)",
                (datum, liter, preis, km),
            )
            self.conn.commit()
            self.conn.close()
        except Exception as e:
            messagebox.showerror("Fehler", str(e))
        finally:
            self.conn.close()
        messagebox.showinfo("Gespeichert", "Tankvorgang gespeichert")
