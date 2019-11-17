import falcon
from falcon import testing
import pytest
import json

from SimpleAssetManager.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_list_assets(client):
    response = client.simulate_get('/assets')
    result_doc = json.loads(response.content)
    result_doc = result_doc['assets'][0]['id']
    expected = 1
    assert result_doc == expected
    assert response.status == falcon.HTTP_OK
