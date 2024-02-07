import tkinter as tk
from views.tankvorgaenge_view import Tankvorgaenge
from tkinter import ttk
from database.database import Database

# Initialisieren der Datenbank und Erstellen der Tabellen
db = Database()
db.create_tables()


def main():
    root = tk.Tk()
    root.title("Hauptseite")
    root.geometry("400x300+100+100")  # Breite x Höhe + X-Position + Y-Position
    root.resizable(width=False, height=False)  # Fenstergröße ist nicht veränderbar

    # Funktion zum Öffnen des Tankvorgänge-Fensters
    def open_tankvorgaenge():
        Tankvorgaenge(root)

    # Weitere Funktionen für andere Unterseiten hier definieren...

    # Dictionary mit Button-Texten und zugehörigen Funktionen
    buttons_config = {
        "Tankvorgänge": open_tankvorgaenge,
        # Weitere Buttons und Funktionen hier hinzufügen
    }

    # Funktion zum Erstellen von Buttons basierend auf der Konfiguration
    def create_buttons(config):
        for text, command in config.items():
            button = ttk.Button(root, text=text, command=command)
            button.pack(pady=5)

    # Buttons basierend auf der Konfiguration erstellen
    create_buttons(buttons_config)

    root.mainloop()


if __name__ == "__main__":
    main()
