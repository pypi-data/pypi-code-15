import requests
from requests.auth import AuthBase
from nameko.extensions import DependencyProvider


class ObjectStorage(DependencyProvider):
    def __init__(self, config=None):
        self.config = config

    def setup(self):
        if not self.config:
            self.config = self.container.config['OBJECT_STORAGE']

    def get_dependency(self, worker_ctx):
        return Connection(self.config)


class Connection(object):
    def __init__(self, config):
        self.config = config
        self.auth = self._get_auth()

    def get_object(self, container, object_name):
        url = self._construct_object_url(container, object_name)
        # TODO: chunk download! Probably using closing

        r = requests.get(url, auth=self.auth)
        return [line.decode('utf-8') for line in r.iter_lines()]

    def _construct_object_url(self, container, object_name):
        return 'https://{0}/{1}/AUTH_{2}/{3}/{4}'.format(
            self.config['access_point'],
            self.config['api_version'],
            self.config['project_id'],
            container,
            object_name
        )

    def _get_auth(self):
        token = self._get_auth_token()
        return XTokenAuth(token)

    def _get_auth_token(self):
        auth_token_url = 'https://identity.open.softlayer.com/v3/auth/tokens'
        payload = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "id": self.config['username'],
                            "password": self.config['password']
                        }
                    }
                },
                "scope": {
                    "project": {
                        "id": self.config['project_id']
                    }
                }
            }
        }

        res = requests.post(auth_token_url, json=payload)
        return res.headers['X-Subject-Token']


class XTokenAuth(AuthBase):
    '''Attaches X-Auth-token to the given Request object.
    '''

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['X-Auth-Token'] = self.token
        return r
