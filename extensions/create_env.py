import os
import requests
from cachetools import TTLCache
from shared_dependencies import API_URL, API_KEY

# Token cache to reduce API token usage
# Cache with TTL of 12 hours
TOKEN_CACHE = TTLCache(maxsize=100, ttl=12 * 60 * 60)

class CreateEnvExtension:
    def __init__(self):
        self.environment_name = ''

    def set_environment_name(self, name):
        self.environment_name = name

    def create_environment(self):
        if os.geteuid() != 0:
            raise PermissionError('Sudo privileges are required to create environments.')
        # Check if the token is in the cache
        token = TOKEN_CACHE.get('api_token')
        if not token:
            # If not in cache, request new token and store it
            token = self.request_new_token()
            TOKEN_CACHE['api_token'] = token
        # Use the token to create the environment
        response = requests.post(f'{API_URL}/environments', headers={'Authorization': f'Bearer {token}'}, json={'name': self.environment_name})
        if response.status_code == 201:
            print(f"Environment '{self.environment_name}' created successfully.")
        else:
            print(f"Failed to create environment: {response.text}")

    def request_new_token(self):
        # Requesting a new API token
        response = requests.post(f'{API_URL}/auth/token', json={'api_key': API_KEY})
        if response.status_code == 200:
            return response.json().get('token')
        else:
            raise Exception(f"Failed to retrieve API token: {response.text}")

    def open_extension(self):
        # Placeholder for opening the extension in the Gemini terminal
        pass

    def close_extension(self):
        # Placeholder for closing the extension in the Gemini terminal
        pass
