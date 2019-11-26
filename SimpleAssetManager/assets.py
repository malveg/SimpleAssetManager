import json
import falcon

from .models.assets_model import Assets

class Resource(object):

    def on_get(self, req, resp):
        al = self.session.query(Assets).all()
        disp = [g.to_dict() for g in al]
        doc = {
            'assets':  disp
        }
        resp.body = json.dumps(doc, ensure_ascii=True)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp):
        payload = req.media.get('payload')
        ids_to_delete = payload['ids_to_delete']

        asset_list = self.session.query(Assets).filter( Assets.id.in_(ids_to_delete) ).all()
        for a in asset_list:
            self.session.delete(a)

        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        payload = req.media.get('payload')
        if payload != None:
            names_to_add = payload['names']
            for name in names_to_add:
                asset = Assets(name=name)
                self.session.add(asset)
            resp.status = falcon.HTTP_200
        else:
            resp.status = falcon.HTTP_404

    def on_put(self, req, resp):
        payload = req.media.get('payload')
        id = payload['id']
        new_name = payload['new_name']
        asset = self.session.query(Assets).filter_by(id=id).first()
        asset.name = new_name
        resp.status = falcon.HTTP_200
