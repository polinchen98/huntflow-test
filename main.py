import argparse
from parser import parse, parse_applicants
from api_service import post_applicants, set_auth
import pprint


parser = argparse.ArgumentParser()
parser.add_argument('--token', dest='token', type=str, help='Authorization token', required=True)
parser.add_argument('--folder', dest='folder', type=str, help='Path to folder with candidates', required=True)
args = parser.parse_args()

set_auth(args.token)

applicants = parse_applicants(parse(args.folder))

for applicant in applicants:
    r = post_applicants(applicant)

    pprint.pprint(r.json())
