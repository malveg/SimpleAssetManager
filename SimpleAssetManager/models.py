import os
from sqlalchemy import create_engine
from sqlalchemy.sql import func


def get_engine():
    # Database file location
    DEFAULT_PATH = os.path.join(os.path.dirname(__file__),'data', 'SimpleAssetManDB.sqlite3')

    # Engine Mechanism
    engine = create_engine("sqlite:///"+DEFAULT_PATH)


def init_db():
    eng = get_engine()
    Base.metadata.create_all(eng)


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
