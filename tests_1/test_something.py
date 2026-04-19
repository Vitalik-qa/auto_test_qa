import requests
from tests_1.config.configuration import SERVICE_URL
from tests_1.config.response import Response
from tests_1.schemas.post import POST_SCHEMA


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)
