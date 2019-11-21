from .db_util_sa import *

class AssetList(object):
    # def __init__(self):
    #     init_db()

    def GetAllAssets(self):
        results = get_all_assets()
        d = []
        for r in results:
            d.append(r.to_dict())
        print(d)
        return d

    def AddAsset(self,asset_name):
        return create_asset(asset_name)

    def UpdateAsset(self,asset_id, field, value):
        return update_asset(asset_id,field,value)

    def RemoveAsset(self,asset_id_list):
        return remove_assets(asset_id_list)

    def PrintAllAssets(self):
        assets = get_all_assets()
        for asset in assets:
            print(asset)
