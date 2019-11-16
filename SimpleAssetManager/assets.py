import json
import falcon

class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'assets':[
                {'id':'23230','name':'test asset 23230','createdate':'mmddadgyayg','updateddate':'324302'}
            ]
        }
        resp.body = json.dumps(doc)
        resp.status = falcon.HTTP_200
