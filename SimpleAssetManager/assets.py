import json
import falcon

from .AssetList import AssetList

class Resource(object):

    def on_get(self, req, resp):
        al = AssetList()
        assets = al.GetAllAssets()
        doc = {
            'assets':  assets
        }
        resp.body = json.dumps(doc, ensure_ascii=True)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        al = AssetList()
        idlist = range(2,50)
        assets = al.RemoveAsset(idlist)
        #get remaining
        assets = al.GetAllAssets()
        doc = {
            'assets':  assets
        }
        resp.body = json.dumps(doc)
        resp.status = falcon.HTTP_200
