import argparse
import os
from scraper import scrape
from search import search
from output import output

BASE_URL = 'http://www.artsci.utoronto.ca/current/exams/{}'

parser = argparse.ArgumentParser(description='UofT Exam Schedule scraper')
parser.add_argument('-s', dest="semester", type=str, default='W16',
                    help='semester / year to get schedule for \
                          (format: SYY, default: W16)')
parser.add_argument('-c', dest='courses', nargs='+', required=True,
                    help='courses (separated by a space, use dash for \
                          lecture code) [eg. csc148-l0101 csc165]')
parser.add_argument('-ln', dest='last_name', type=str, required=True,
                    help='last name')
parser.add_argument('-f', dest='format', type=str, default='raw',
                    choices=['raw', 'table', 'json'],
                    help='output format (one of <table|json|raw>)')


def main():
    args = parser.parse_args()
    courses, ln, date = args.courses, args.last_name, \
        ('apr' if args.semester[0] == 'W' else 'dec') + args.semester[1:]

    exam_data = scrape(BASE_URL.format(date))
    if exam_data is not None:
        user_exams = search(exam_data, courses, ln)
        if user_exams is not None:
            return output(user_exams, args.format, str(ln + '.{}'))
        return print('Couln\'t find exam information for given courses.')
    return print('Couldn\'t find exam information for given semester.')


if __name__ == '__main__':
    main()
