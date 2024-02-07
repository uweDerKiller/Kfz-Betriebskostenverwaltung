import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class TankvorgaengeView:
    def __init__(self, master):
        self.master = master
        self.master.title("Tankvorgänge")

        tk.Label(self.master, text="Datum:").grid(row=0, column=0)
        self.datum_entry = tk.Entry(self.master)
        self.datum_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Liter:").grid(row=1, column=0)
        self.liter_entry = tk.Entry(self.master)
        self.liter_entry.grid(row=1, column=1)

        tk.Label(self.master, text="Preis pro Liter:").grid(row=2, column=0)
        self.preis_entry = tk.Entry(self.master)
        self.preis_entry.grid(row=2, column=1)

        tk.Label(self.master, text="Gefahrene Kilometer:").grid(row=3, column=0)
        self.km_entry = tk.Entry(self.master)
        self.km_entry.grid(row=3, column=1)

        ttk.Button(self.master, text="Speichern", command=self.speichern).grid(
            row=4, column=0, columnspan=2
        )

    def speichern(self):
        datum = self.datum_entry.get()
        liter = self.liter_entry.get()
        preis = self.preis_entry.get()
        km = self.km_entry.get()

        try:
            datetime.strptime(datum, "%Y-%m-%d")  # (YYYY-MM-DD)
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

        # Hier können Sie die Daten speichern (z. B. in einer Datenbank)
        # Fügen Sie Ihre Speicherlogik hier ein

        messagebox.showinfo("Gespeichert", "Tankvorgang gespeichert")
