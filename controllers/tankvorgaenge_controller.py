from tkinter import messagebox
import datetime


class TankvorgaengeController:
    def __init__(self, view):
        self.view = view

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

            # Hier können Sie die Logik für das Speichern der Daten (z. B. in einer Datenbank) hinzufügen
            # Zeigen Sie eine Erfolgsmeldung oder Fehlermeldung basierend auf dem Speicherergebnis an
            messagebox.showinfo("Gespeichert", "Tankvorgang gespeichert")
