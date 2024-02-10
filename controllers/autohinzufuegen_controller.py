# autohinzufuegen_controller.py

from datetime import datetime
from tkinter import messagebox
import sqlite3
from models.auto import Kennzeichen


class AutoHinzufuegenController:
    def __init__(self, view):
        self.view = view

    def speichern(self, marke, modell, baujahr, kennzeichen):
        try:
            datetime.strptime(baujahr, "%Y")  # Prüfe das Datumsformat
        except ValueError:
            messagebox.showerror("Fehler", "Ungültiges Datumsformat")
            return
        kennzeichen_obj = Kennzeichen(kennzeichen)
        if not kennzeichen_obj.is_valid():
            messagebox.showerror("Fehler", "Ungültiges Kennzeichen")
            return
        conn = sqlite3.connect("meine_datenbank.db")
        c = conn.cursor()
        c.execute(
            """CREATE TABLE IF NOT EXISTS autos
                (marke TEXT, modell TEXT, baujahr INTEGER, kennzeichen TEXT)"""
        )
        c.execute(
            "INSERT INTO autos (marke, modell, baujahr, kennzeichen) VALUES (?, ?, ?, ?)",
            (marke, modell, baujahr, str(kennzeichen_obj)),
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Gespeichert", "Auto gespeichert")
