import os
import falcon

from .config import config_dict
from .db import SQLAlchemyMiddleware

from .assets import Resource


#curl -X POST http://localhost:8080/assets --header "Content-Type: application/json" -d @test.json

def create_app(environment_name):
    configuration = config_dict[environment_name]
    falcon_api = falcon.API(middleware=[
        SQLAlchemyMiddleware(configuration)
    ])
    assets = Resource()
    falcon_api.add_route('/assets', assets)
    return falcon_api, configuration


api, config = create_app(os.getenv('APP_ENV') or 'default')
