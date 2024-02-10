from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    Date,
    Text,
)
from sqlalchemy.orm import relationship
from database.database import (
    Base,
)  # Importieren Sie Base von database.pyfrom database import Database


class Tankvorgang(Base):
    __tablename__ = "tankvorgaenge"
    id = Column(Integer, primary_key=True)
    auto_id = Column(Integer, ForeignKey("autos.id"))
    datum = Column(Date)
    liter = Column(Float)
    preis = Column(Float)
    gefahrene_km = Column(Float)

    auto = relationship("Auto", back_populates="tankvorgaenge")
