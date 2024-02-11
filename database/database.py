from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.config import DATABASE_URL

Base = declarative_base()


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

    def get_available_autos(self):
        from models.auto import Auto

        session = self.Session()
        autos = session.query(Auto).all()
        session.close
        return [auto.marke + " " + auto.modell for auto in autos]

    def get_all_tankvorgaenge(self):
        from models.tankvorgang import Tankvorgang

        session = self.Session()
        tankvorgaenge = session.query(Tankvorgang).all()
        session.close()

        return tankvorgaenge
