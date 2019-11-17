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
        payload = req.media.get('payload')
        ids_to_delete = payload['ids_to_delete']
        al = AssetList()
        al.RemoveAsset(ids_to_delete)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        payload = req.media.get('payload')
        names_to_add = payload['names']
        al = AssetList()
        for name in names_to_add:
            al.AddAsset(name)
        resp.status = falcon.HTTP_200

    def on_put(self, req, resp):
        payload = req.media.get('payload')
        id = payload['id']
        new_name = payload['new_name']
        al = AssetList()
        al.UpdateAsset(id,'name',new_name)
        resp.status = falcon.HTTP_200
