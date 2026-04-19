import requests

from tests.configuration import SERVICE_URL
from tests.global_enums import GlobalErrorMessages

def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    received_pots = response.json()


    assert response.status_code == 200, GlobalErrorMessages.STATUS_CODE.value
    assert len(received_pots) == 3, GlobalErrorMessages.ELEMENT_COUNT.value
    print(response.json())
