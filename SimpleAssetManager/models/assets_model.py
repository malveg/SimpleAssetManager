from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.sql import func
import os

Base=declarative_base()
DB_PATH = os.path.join('..','data', 'SimpleAssetManDB.sqlite3')
DB_URI = "sqlite:///" + DB_PATH


class Assets(Base):
    __tablename__ = 'assets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_added = Column(DateTime, server_default=func.now())
    last_modified = Column(DateTime, server_default=func.now(), onupdate=func.now())

    def to_dict(self):
        d = {}
        d['id'] = self.id
        d['name'] = self.name
        d['date_added'] = str(self.date_added)
        d['last_modified'] =str(self.last_modified)
        return d

if __name__=="__main__":
    from sqlalchemy import create_engine
    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
