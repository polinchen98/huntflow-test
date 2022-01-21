import json
import requests

headers = {'User-Agent': 'huntflow-test-app (incaseoffire@example.com)'}

api_url = 'https://dev-100-api.huntflow.dev'


def set_auth(token):
    headers['Authorization'] = f'Bearer {token}'


def post_applicants(applicant):
    return requests.post(f'{api_url}/account/2/applicants', data=json.dumps(applicant), headers=headers)
