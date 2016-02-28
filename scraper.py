import requests
from bs4 import BeautifulSoup


def scrape(url):
    return parse(request(url))


def request(url):
    return requests.get(url=url)


def parse(resp):
    courses = []
    soup = BeautifulSoup(resp.text, 'html.parser')
    rows = soup.find('div', id='content').find('table').find_all('tr')
    headers = [col.text.lower() for col in rows[0].find_all('th')]
    for row in rows[1:]:
        td = [col.text for col in row.find_all('td')]
        course = {}
        for i in range(len(headers)):
            course[headers[i]] = td[i]
        courses.append(course)
    return courses


if __name__ == '__main__':
    url = 'http://www.artsci.utoronto.ca/current/exams/apr16'
    scrape(url)
