#db_utils using SqlAlchemy
import os
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

DEFAULT_PATH = os.path.join(os.path.dirname(__file__),'data', 'SimpleAssetManDB.sqlite3')

engine = create_engine("sqlite:///"+DEFAULT_PATH)
Base = declarative_base()
Base.metadata.create_all(engine)
session = Session(bind=engine)

##############################################################################
#using the ORM
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

def init_db():
    Base.metadata.create_all(engine)


def create_asset(n):
    asset = Assets(name=n)
    session.add(asset)
    session.commit()
    return asset

def update_asset(id,field,value):
    asset = session.query(Assets).filter_by(id=id).first()
    asset.name = value
    session.commit()
    return asset


def remove_assets(asset_id_list):
    asset_list = session.query(Assets).filter( Assets.id.in_(asset_id_list) ).all()
    for a in asset_list:
        session.delete(a)
    session.commit()


def get_all_assets():
    query = session.query(Assets).all()
    return query

def get_asset(id):
    query = session.query(Assets).filter(Asset.id == id).first()
    return query

##############################################################################
#using MetaData() and Table()
# def init_db():
#     engine = get_engine()
#     metadata = MetaData()
#     assets_table = Table('assets', metadata,
#             Column('id', Integer, primary_key=True),
#             Column('name', String),
#             Column('date_added', DateTime),
#             Column('last_modified', DateTime)
#         )
#     metadata.create_all(engine)


##############################################################################
# raw engine
# def raw_init_db():
#     confirm_sql = "SELECT name FROM sqlite_master WHERE type='table'"
#     result = engine.execute("SELECT name FROM sqlite_master WHERE type='table'")
#     if result is None:
#         create_assets_table()
#
#
# def raw_create_assets_table():
#     make_assets_sql = "CREATE TABLE assets (id INTEGER PRIMARY KEY, name TEXT NOT NULL, date_added TEXT NOT NULL DEFAULT (datetime('now')), last_modified TEXT DEFAULT (datetime('now'))  ) "
#     engine.execute(make_assets_sql)
#     make_assets_trigger_sql = "CREATE TRIGGER update_assets_lastmodified UPDATE ON assets BEGIN UPDATE assets SET last_modified = (datetime('now')) WHERE id = old.id; END"
#     engine.execute(make_assets_trigger_sql)
