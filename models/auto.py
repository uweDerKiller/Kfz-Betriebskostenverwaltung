# models/auto.py

import re


class Kennzeichen:
    def __init__(self, kennzeichen):
        self.kennzeichen = kennzeichen

    def is_valid(self):
        # Überprüfe, ob das Kennzeichen dem festgelegten Format entspricht
        pattern = r"^[A-Z]{1,2}-[A-Z]{1,2}\s\d{1,4}$"
        return bool(re.match(pattern, self.kennzeichen))

    def __str__(self):
        return self.kennzeichen


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base, Database  # Importiere Base von database.py
from .tankvorgang import Tankvorgang
from .werkstattrechnung import Werkstattrechnung


class Auto(Base):
    __tablename__ = "autos"
    id = Column(Integer, primary_key=True)
    marke = Column(String)
    modell = Column(String)
    baujahr = Column(Integer)
    kennzeichen = Column(String)

    # Weitere Definitionen...
    tankvorgaenge = relationship(
        "Tankvorgang", order_by=Tankvorgang.id, back_populates="auto"
    )
    werkstattrechnungen = relationship(
        "Werkstattrechnung", order_by=Werkstattrechnung.id, back_populates="auto"
    )
