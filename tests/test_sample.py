from http import HTTPStatus

import requests


class TestSample:
    def test_sample(self, app_url):
        response = requests.get(app_url)
        assert response.status_code == HTTPStatus.OK
