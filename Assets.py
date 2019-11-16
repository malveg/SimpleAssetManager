import db_utils as db

class AssetList(object):
    def __init__(self):
        db.init_assets_table()

    def GetAllAssets(self):
        return db.get_all_assets()

    def AddAsset(self,asset_name):
        return db.create_asset(asset_name)

    def UpdateAsset(self,asset_id, field, value):
        return db.update_asset(asset_id,field,value)

    def RemoveAsset(self,asset_id_list):
        return db.remove_assets(asset_id_list)

    def PrintAllAssets(self):
        db.display_assets()
