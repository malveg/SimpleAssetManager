import falcon
from .assets import Resource




api = falcon.API()

assets = Resource()

api.add_route('/assets', assets)
