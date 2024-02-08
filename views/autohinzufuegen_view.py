import tkinter as tk
from tkinter import ttk, messagebox
from controllers.autohinzufuegen_controller import AutoHinzufuegenController


class AutoHinzufuegenView:
    def __init__(self, master):
        self.master = master
        self.master.title("Auto hinzufügen")
        tk.Label(self.master, text="Marke").grid(row=0, column=0)
        self.marke_entry = tk.Entry(self.master)
        self.marke_entry.grid(row=0, column=1)
        tk.Label(self.master, text="Modell").grid(row=1, column=0)
        self.modell_entry = tk.Entry(self.master)
        self.modell_entry.grid(row=1, column=1)
        tk.Label(self.master, text="Baujahr").grid(row=2, column=0)
        self.baujahr_entry = tk.Entry(self.master)
        self.baujahr_entry.grid(row=2, column=1)
        tk.Label(self.master, text="Kennzeichen").grid(row=3, column=0)
        self.kennzeichen_entry = tk.Entry(self.master)
        self.kennzeichen_entry.grid(row=3, column=1)
        ttk.Button(self.master, text="Speichern", command=self.speichern).grid(
            row=4, column=0, columnspan=2
        )
        # Controller initialisieren
        self.controller = AutoHinzufuegenController(self)

    def speichern(self):
        modell = self.modell_entry.get()
        marke = self.marke_entry.get()
        baujahr = self.baujahr_entry.get()
        kennzeichen = self.kennzeichen_entry.get()

        self.controller.speichern(marke, modell, baujahr, kennzeichen)
