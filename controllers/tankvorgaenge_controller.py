import sqlite3
from tkinter import messagebox
import datetime


def tankvorgang_speichern(datum, liter, preis, gefahrene_km):
    if not isinstance(datum, datetime.date):
        messagebox.showerror("Fehler", "Ungültiges Datumsformat")
        return
    liter = convert_to_float(liter)
    preis = convert_to_float(preis)
    gefahrene_km = convert_to_float(gefahrene_km)
    if liter is None or preis is None or gefahrene_km is None:
        messagebox.showerror("Fehler", "Ungültige numerische Eingabe")
        return
    try:
        conn = sqlite3.connect("meine_datenbank.db")
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS tankvorgaenge
                    (datum TEXT, liter FLOAT, preis FLOAT, gefahrene_km FLOAT)"""
        )
        c.execute(
            "INSERT INTO tankvorgaenge (datum, liter, preis, gefahrene_km) VALUES (?, ?, ?, ?)",
            (datum, liter, preis, gefahrene_km),
        )
        conn.commit()
        messagebox.showinfo("Gespeichert", "Tankvorgang gespeichert")
    except sqlite3.Error as e:
        messagebox.showerror("Fehler", "Datenbankfehler: " + str(e))
    finally:
        conn.close()


def convert_to_float(entry):

    print("entry vor strip" + str(entry))
    entry_text = entry.strip()
    print("entry_text" + str(entry_text))
    if not entry_text:  # Prüfen Sie, ob der Text leer ist
        return None
    entry_text = entry_text.replace(",", ".")
    print("entry_text replaced" + str(entry_text))
    try:
        float_value = float(entry_text)
        print("und konvertiert" + str(float_value))
        return float_value
    except ValueError:
        return None
