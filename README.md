# SimpleAssetManager
An exploration in SQLite, SqlAlchemy and Falcon to create a simple CRUD API

## Setup
### Install falcon and SqlAlchemy
    $pip install falcon
    $pip install sqlalchemy

### Navigate to models folder and generate SQLite DB
    $cd SimpleAssetManager/SimpleAssetManager/models
    $python assets_model.py

### Install optional features
    $pip install pytest
    $pip install waitress

### Run Server
From inside root folder:

    $waitress-serve --port=8080 SimpleAssetManager.app:api
