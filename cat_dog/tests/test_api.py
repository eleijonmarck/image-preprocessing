import http.client


class Tests():
    def test_not_authenticated(self):
        self.client.authorization = None
        response = self.client.post('/')
        assert response.status_code == http.client.UNAUTHORIZED
        assert 'WWW-Authenticate' in response.headers
        assert 'Basic' in response.headers['WWW-Authenticate']

    def test_wrongly_authenticated(self):
        self.client.authorization = ('foo', 'foo')
        response = self.client.post('/')
        assert response.status_code == http.client.UNAUTHORIZED
        assert 'WWW-Authenticate' in response.headers
        assert 'Basic' in response.headers['WWW-Authenticate']

    def test_authenticated(self):
        response = self.client.post('/')
        assert response.status_code == http.client.OK
