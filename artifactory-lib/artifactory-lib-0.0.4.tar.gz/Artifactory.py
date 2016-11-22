import requests

class Artifactory(object):
    """Artifactory Management Tool"""
    def __init__(self, username, apikey, base_url='https://localhost:8080/artifactory'):
        self.username = self.set_username(username)
        self.apikey   = self.set_apikey(apikey)
        self.base_url = self.set_base_url(base_url)

    def __str__(self):
        return 'Artifactory: %s @ %s' % (self.username, self.base_url)

    def __repr__(self):
        return '<Artifactory user:%s url:%s>' % (self.username, self.base_url)

    ''' Internal Setters '''
    def set_username(self, username):
        self.username = username

    def set_apikey(self, apikey):
        self.apikey = apikey

    def set_base_url(self, base_url):
        self.base_url = base_url.rstrip('/')

    '''Internal Getters'''
    def get_username(self):
        return self.username

    def get_apikey(self):
        return self.apikey

    def get_base_url(self):
        return self.base_url

    ''' Helper functions '''
    def build_url(self, endpoint):
        return ''.join([
            self.base_url,
            '/api',
            endpoint
        ])

    def get(self, endpoint):
        r = requests.get(self.build_url(endpoint), auth=(self.username, self.apikey))
        if r.status_code is 200:
            return r.json()

    def post(self, endpoint):
        r = requests.post(self.build_url(endpoint), auth=(self.username, self.apikey))
        if r.status_code is 200:
            return r.json()

    def put(self, endpoint, data={}):
        r = requests.put(
            self.build_url(endpoint),
            auth=(self.username, self.apikey),
            json=data
        )
        if r.status_code is 200:
            return r.json()

    def delete(self, endpoint):
        r = requests.delete(self.build_url(endpoint), auth=(self.username, self.apikey))
        if r.status_code is 200:
            return r.text

    '''
    Security Section
    https://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API#ArtifactoryRESTAPI-SECURITY ###
    '''
    def get_users(self):
        return self.get('/security/users')

    def get_user(self, username):
        return self.get('/security/users/%s' % username)

    def create_user(self, username):
        return self.put('/security/users/%s' % username.lower(), {
            'email': '%s@email.com' % username,
            'password': 'password'
        })

    def delete_user(self, username):
        return self.delete('/security/users/%s' % username.lower())

    def get_api_key(self):
        return self.get('/security/apiKey')

    def create_api_key(self):
        return self.post('/security/apiKey')

    def regenerate_api_key(self):
        return self.put('/security/apiKey')

    def revoke_api_key(self):
        return self.delete('/security/apiKey')
