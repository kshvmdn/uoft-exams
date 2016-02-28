import json
import argparse
from scraper import scrape
from search import search
from pprint import pprint

BASE_URL = 'http://www.artsci.utoronto.ca/current/exams/{}'

parser = argparse.ArgumentParser(description='UofT Exam Schedule scraper')
parser.add_argument('-s', dest="semester", type=str, default='W16',
                    help='semester / year to get schedule for \
                          (format: SYY, default: W16)')
parser.add_argument('-c', dest='courses', nargs='+', required=True,
                    help='courses (separated by a space)')
parser.add_argument('-ln', dest='last_name', type=str, required=True,
                    help='last name')


def main():
    args = parser.parse_args()
    date = ('apr' if args.semester[0] == 'W' else 'dec') + args.semester[1:]
    ln = args.last_name

    courses = scrape(BASE_URL.format(date))

    if courses is not None:
        courses = search(courses, args.courses, ln)
        pprint(courses)
    else:
        print('Couldn\'t find schedule data for given date.')


if __name__ == '__main__':
    main()
