import argparse
import json
from parser import parse, parse_applicants
from api_service import post_applicants, set_auth, get_vacancies, get_statuses, post_resume, add_applicant_to_vacancy
import os

parser = argparse.ArgumentParser()
parser.add_argument('--token', dest='token', type=str, help='Authorization token', required=True)
parser.add_argument('--folder', dest='folder', type=str, help='Path to folder with candidates', required=True)
args = parser.parse_args()

set_auth(args.token)

applicants, extra = parse_applicants(parse(args.folder))
positions = set()

applicants_with_id = []

for applicant in applicants:
    positions.add(applicant['position'])
    r = post_applicants(applicant)
    applicants_with_id.append(r.json())

names_to_resume_id = {}

for position in positions:
    resumes = os.listdir(f'{args.folder}/{position}')
    for resume in resumes:
        resume_with_id = post_resume(f'{args.folder}/{position}/{resume}')
        full_name = json.loads(resume_with_id)['name']
        full_name = str(full_name).split('.')[0].strip()
        id = json.loads(resume_with_id)['id']
        names_to_resume_id[full_name] = id

position_to_vacancy_id = {}

vacancies = get_vacancies()
for vacancy in vacancies:
    vacancy_id = vacancy['id']
    position = vacancy['position']
    position_to_vacancy_id[position] = id

name_to_status = {}

statuses = get_statuses()
for status in statuses:
    status_id = status['id']
    name = status['name']
    name_to_status[name] = id

for i, applicant in enumerate(applicants_with_id):

    applicant_id = applicant['id']
    vacancy_id = position_to_vacancy_id[applicant["position"]]
    status_id = name_to_status[extra[i]['status']]
    comment = extra[i]['comment']
    resume_id = names_to_resume_id[extra[i]['full_name']]

    add_applicant_to_vacancy(vacancy_id, status_id, comment, resume_id, applicant_id)

