import argparse
from parser import parse, parse_applicants
from api_service import post_applicants, set_auth, get_vacancies, get_statuses, post_resume
import pprint

parser = argparse.ArgumentParser()
parser.add_argument('--token', dest='token', type=str, help='Authorization token', required=True)
parser.add_argument('--folder', dest='folder', type=str, help='Path to folder with candidates', required=True)
args = parser.parse_args()

set_auth(args.token)

applicants = parse_applicants(parse(args.folder))

for applicant in applicants:
    r = post_applicants(applicant)
    applicants_with_id = r.json()

vacancies = get_vacancies()
for vacancy in vacancies:
    id = vacancy['id']
    position = vacancy['position']
    print(id, position)

statuses = get_statuses()
for status in statuses:
    id = status['id']
    name = status['name']
