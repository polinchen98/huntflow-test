import json
import subprocess
import requests

headers = {'User-Agent': 'huntflow-test-app (incaseoffire@example.com)'}
api_url = 'https://dev-100-api.huntflow.dev'
account_id = 2


def set_auth(token):
    headers['Authorization'] = f'Bearer {token}'


def post_applicants(applicant):
    return requests.post(f'{api_url}/account/{account_id}/applicants', data=json.dumps(applicant), headers=headers)


def get_vacancies():
    r = requests.get(f'{api_url}/account/{account_id}/vacancies', headers=headers).json()
    return r['items']


def get_statuses():
    r = requests.get(f'{api_url}/account/{account_id}/vacancy/statuses', headers=headers).json()
    return r['items']


def post_resume(path_to_resume):
    request = ['curl', '-X', 'POST',
               '-H', "Content-Type: multipart/form-data",
               '-H', "X-File-Parse: true",
               '-H', f"Authorization: {headers['Authorization']}",
               '-F', f"file=@{path_to_resume}",
               f'{api_url}/account/{account_id}/upload']
    return subprocess.call(request)
