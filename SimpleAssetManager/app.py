import falcon
from waitress import serve

from assets import Resource




api = falcon.API()

assets = Resource()

api.add_route('/assets', assets)

serve(api, listen='*:8080')
