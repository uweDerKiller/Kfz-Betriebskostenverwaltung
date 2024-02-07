# models/auto.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ..database.database import Base  # Importieren Sie Base von database.py
from tankvorgang import Tankvorgang
from werkstattrechnung import Werkstattrechnung


class Auto(Base):
    __tablename__ = "autos"
    id = Column(Integer, primary_key=True)
    marke = Column(String)
    modell = Column(String)
    baujahr = Column(Integer)
    kennzeichen = Column(String)

    # Vorherige Definitionen...
    tankvorgaenge = relationship(
        "Tankvorgang", order_by=Tankvorgang.id, back_populates="auto"
    )
    werkstattrechnungen = relationship(
        "Werkstattrechnung", order_by=Werkstattrechnung.id, back_populates="auto"
    )
