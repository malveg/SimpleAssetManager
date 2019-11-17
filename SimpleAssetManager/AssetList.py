from .db_utils import *

class AssetList(object):
    def __init__(self):
        init_assets_table()

    def GetAllAssets(self):
        results = []
        rows, columns = get_all_assets()
        for row in rows:
            results.append( dict(zip(columns,row)) )
        return results

    def AddAsset(self,asset_name):
        return create_asset(asset_name)

    def UpdateAsset(self,asset_id, field, value):
        return update_asset(asset_id,field,value)

    def RemoveAsset(self,asset_id_list):
        return remove_assets(asset_id_list)

    def PrintAllAssets(self):
        display_assets()
