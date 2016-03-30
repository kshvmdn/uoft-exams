#!/usr/bin/env python3
import argparse
import sys

from scraper import scrape
from search import search
from output import output

BASE_URL = 'http://www.artsci.utoronto.ca/current/exams/{}'

parser = argparse.ArgumentParser(description='UofT Exam Schedule scraper')
parser.add_argument('-s', '--semester',
                    dest="semester",
                    type=str,
                    default='W16',
                    help='semester (S) + year (YY) to get schedule for \
                          (format: SYY) [default: W16]')
parser.add_argument('-c', '--courses',
                    dest='courses',
                    nargs='+',
                    required=True,
                    help='courses (separated by a space, use dash for \
                          lecture code) [eg. csc148-l0101 csc165]')
parser.add_argument('-n', '--name',
                    dest='last_name',
                    type=str,
                    required=True,
                    help='last name')
parser.add_argument('-f', '--format',
                    dest='format',
                    type=str, default=None,
                    choices=['table', 'json'],
                    help='output format (one of <table|json>) [default: None]')


def main():
    args = parser.parse_args()
    courses, ln, season, year, format_ = args.courses, args.last_name, \
        args.semester[0], args.semester[1:], args.format

    if season.upper() not in ('W', 'F') or not year.isnumeric():
        print('Unexpected semester argument (run -h for details).')
        sys.exit(1)

    date = ('apr' if season == 'W' else 'dec') + year

    exam_data = scrape(BASE_URL.format(date))
    if exam_data is not None:
        user_exams = search(exam_data, courses, ln)
        if user_exams is not None:
            return output(user_exams, format_, '{}-exams'.format(ln) + '.{}')
        else:
            print('Couldn\'t find exam information for given courses.')
            sys.exit(1)
    else:
        print('Couldn\'t find exam information for given semester.')
        sys.exit(1)

if __name__ == '__main__':
    main()
