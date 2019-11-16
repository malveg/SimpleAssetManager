# db_utils.py
import os
import sqlite3

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__),'data', 'SimpleAssetManDB.sqlite3')

def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

def db_open_assets():
    con = db_connect()
    cur = con.cursor()
    return con,cur

def init_assets_table():
    con,cur = db_open_assets()

    def init_confirm_assets_table(con,cur):
        try:
            confirm_sql = "SELECT name FROM sqlite_master WHERE type='table'"
            cur.execute(confirm_sql)
            tables = cur.fetchall()[0]
            if 'assets' in tables:
                return 0
            else:
                raise("assets Table does not exist")
        except:
            return 1
    #---------------------------------------------------------------
    #Check for table
    if init_confirm_assets_table(con,cur) != 0:
        #assets table needs to be created
        try:
            #Create a table to manage assets
            assets_sql = "CREATE TABLE assets (id INTEGER PRIMARY KEY, name TEXT NOT NULL, date_added TEXT NOT NULL DEFAULT (datetime('now')), last_modified TEXT DEFAULT (datetime('now'))  ) "
            cur.execute(assets_sql)
            #Create a trigger to manage update time
            sql = "CREATE TRIGGER update_assets_lastmodified UPDATE ON assets BEGIN UPDATE assets SET last_modified = (datetime('now')) WHERE id = old.id; END"
            cur.execute(sql)
            con.commit()
        except:
            con.rollback()
            raise RuntimeError("Could not create assets table with trigger.")

        return 0
    else:
        return 0





def get_all_assets():
    sql = "SELECT id, name, date_added, last_modified FROM assets"
    con,cur = db_open_assets()
    cur.execute(sql)
    return cur.fetchall()

def create_asset(asset_name):
    try:
        sql = "INSERT INTO assets (name) VALUES (?)"
        con,cur = db_open_assets()
        cur.execute(sql, (asset_name,))
        #commit ops and return
        con.commit()
        return cur.lastrowid
    except:
        # rollback
        con.rollback()
        raise RuntimeError("ERROR: Could not Insert into assets table")

def update_asset(id, key, value):
    try:
        sql = "UPDATE assets SET "+ key +" = ? WHERE id = ? """
        con,cur = db_open_assets()
        cur.execute(sql, (value,id,))
        #commit ops and return
        con.commit()
        return cur.lastrowid
    except:
        # rollback
        con.rollback()
        raise RuntimeError("ERROR: Could not Update assets table")

def remove_assets(asset_id_list):
    try:
        asset_ids = ','.join(str(x) for x in asset_id_list)
        sql = "DELETE FROM assets WHERE id IN ("+asset_ids+")"
        con,cur = db_open_assets()
        cur.execute(sql)
        #commit ops and return
        con.commit()
        return cur.lastrowid
    except:
        # rollback
        con.rollback()
        raise RuntimeError("ERROR: Could not Update assets table")


def display_assets():
    con = db_open_assets()
    # Print Asset Table
    results = get_all_assets(con)
    for row in results:
        print(row)
