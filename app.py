import tkinter as tk
from tkinter import ttk
from views.tankvorgaenge_view import TankvorgaengeView
from database.database import Database


class App:
    def __init__(self):
        db = Database()
        db.create_tables()
        self.root = tk.Tk()
        self.root.title("Hauptseite")
        self.root.geometry("400x300+100+100")  # Breite x Höhe + X-Position + Y-Position
        self.root.resizable(
            width=False, height=False
        )  # Fenstergröße ist nicht veränderbar
        self._configure_ui()

    def _configure_ui(self):
        buttons_config = {
            "Tankvorgänge": self.open_tankvorgaenge,
            # Weitere Buttons und Funktionen hier hinzufügen
        }

        def create_buttons(config):
            for text, command in config.items():
                button = ttk.Button(self.root, text=text, command=command)
                button.grid()

        create_buttons(buttons_config)

    def open_tankvorgaenge(self):
        # Erstellen eines neuen Top-Level-Fensters für die Tankvorgänge
        new_window = tk.Toplevel(self.root)
        new_window.title("Tankvorgänge")
        new_window.geometry("400x300")  # Sie können die Größe und Position anpassen
        # Initialisieren der Tankvorgänge-Ansicht im neuen Fenster
        TankvorgaengeView(new_window)

    def run(self):
        self.root.mainloop()
