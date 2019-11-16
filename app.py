import falcon
from waitress import serve


class AssetList(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = '{"message": "Asset List"}'



app = falcon.API()

asset_list = AssetList()

app.add_route('/', asset_list)

serve(app, listen='*:8080')
