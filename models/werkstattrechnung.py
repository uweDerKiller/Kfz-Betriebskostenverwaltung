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
from ..database.database import Base  # Importieren Sie Base von database.py


class Werkstattrechnung(Base):
    __tablename__ = "werkstattrechnungen"
    id = Column(Integer, primary_key=True)
    auto_id = Column(Integer, ForeignKey("autos.id"))
    datum = Column(Date)
    beschreibung = Column(Text)
    kosten = Column(Float)

    auto = relationship("Auto", back_populates="werkstattrechnungen")
