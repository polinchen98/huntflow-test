import argparse
import json
from parser import parse, parse_applicants
from api_service import post_applicants, set_auth, get_vacancies, get_statuses, post_resume
import pprint
import os

parser = argparse.ArgumentParser()
parser.add_argument('--token', dest='token', type=str, help='Authorization token', required=True)
parser.add_argument('--folder', dest='folder', type=str, help='Path to folder with candidates', required=True)
args = parser.parse_args()

set_auth(args.token)

applicants = parse_applicants(parse(args.folder))
positions = set()

for applicant in applicants:
    r = post_applicants(applicant)
    applicants_with_id = r.json()
    positions.add(applicant['position'])

for position in positions:
    resumes = os.listdir(f'{args.folder}/{position}')
    for resume in resumes:
        resume_with_id = post_resume(f'{args.folder}/{position}/{resume}')
        name = json.loads(resume_with_id)['name']

vacancies = get_vacancies()
for vacancy in vacancies:
    id = vacancy['id']
    position = vacancy['position']

statuses = get_statuses()
for status in statuses:
    id = status['id']
    name = status['name']
