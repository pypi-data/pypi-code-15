from django.conf import settings
from django.urls import reverse

from requests_oauthlib import OAuth2Session

from .base import OAuthClient


class GoogleOAuth2Client(OAuthClient):
    authorization_base_url = 'https://accounts.google.com/o/oauth2/v2/auth'
    token_url = 'https://www.googleapis.com/oauth2/v4/token'
    scope = [
        'https://www.googleapis.com/auth/userinfo.email',
        'https://www.googleapis.com/auth/userinfo.profile',
    ]
    client_id = settings.GOOGLE_CLIENT_ID
    client_secret = settings.GOOGLE_CLIENT_SECRET

    def __init__(self, request):
        self._request = request
        self._session = OAuth2Session(
            self.client_id,
            scope=self.scope,
            redirect_uri=request.build_absolute_uri(reverse(
                'accounts_oauth2',
                kwargs={'provider': 'google'},
            )),
        )

    def get_authentication_url(self):
        authorization_url, self._state = self._session.authorization_url(
            self.authorization_base_url,
            access_type='offline',  # Only right now.
            # approval_prompt='force',  # Maybe not, later.
        )

        return authorization_url

    def get_user_data(self):
        self._session.fetch_token(
            self.token_url,
            client_secret=self.client_secret,
            authorization_response=self._request.get_full_path(),
        )
        data = self._session.get(
            'https://www.googleapis.com/oauth2/v1/userinfo'
        ).json()

        return {
            'email': data['email'],
            'full_name': data['name'],
        }
