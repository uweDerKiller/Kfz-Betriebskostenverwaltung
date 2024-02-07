import tkinter as tk
from tkinter import ttk, messagebox
import datetime

# from datenmodelle.auto import Auto


class Tankvorgaenge:
    def __init__(self, master):
        # Fenster für Tankvorgänge erstellen
        self.window = tk.Toplevel(master)
        self.window.title("Tankvorgänge")

        # Widgets für die Eingabe erstellen
        tk.Label(self.window, text="Datum:").grid(row=0, column=0)
        self.datum_entry = tk.Entry(self.window)
        self.datum_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Liter:").grid(row=1, column=0)
        self.liter_entry = tk.Entry(self.window)
        self.liter_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Preis pro Liter:").grid(row=2, column=0)
        self.preis_entry = tk.Entry(self.window)
        self.preis_entry.grid(row=2, column=1)

        tk.Label(self.window, text="Gefahrene Kilometer:").grid(row=3, column=0)
        self.km_entry = tk.Entry(self.window)
        self.km_entry.grid(row=3, column=1)

        # Speichern-Button
        ttk.Button(self.window, text="Speichern", command=self.speichern).grid(
            row=4, column=0, columnspan=2
        )

    def speichern(self):
        # Hier würden Sie die Logik implementieren, um die Daten zu speichern
        # Zum Beispiel: Datenvalidierung, Speichern in einer Datei oder Datenbank
        datum = self.datum_entry.get()
        liter = self.liter_entry.get()
        preis = self.preis_entry.get()
        km = self.km_entry.get()
        # Fügen Sie die Validierung und Speicherlogik hier hinzu
        messagebox.showinfo("Gespeichert", "Tankvorgang gespeichert")

        try:
            datetime.strptime(
                datum, "%Y-%m-%d"
            )  # Prüft, ob das Datum im richtigen Format ist (YYYY-MM-DD)
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
