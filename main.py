import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--token', dest='token', type=str, help='Authorization token', required=True)
parser.add_argument('--folder', dest='folder', type=str, help='Path to folder with candidates', required=True)
args = parser.parse_args()

