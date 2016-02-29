import requests
from bs4 import BeautifulSoup


def scrape(url):
    return parse(request(url))


def request(url):
    return requests.get(url=url)


def parse(resp):
    courses = []
    soup = BeautifulSoup(resp.text, 'html.parser')
    if soup.find('div', id='content').find('table'):
        rows = soup.find('div', id='content').find('table').find_all('tr')
        headers = [col.text.lower() for col in rows[0].find_all('th')]
        for row in rows[1:]:
            data = [col.text for col in row.find_all('td')]
            course = dict()
            [course.update({headers[i]: data[i]}) for i in range(len(headers))]
            courses.append(course)
        return courses


if __name__ == '__main__':
    url = 'http://www.artsci.utoronto.ca/current/exams/apr16'
    scrape(url)
