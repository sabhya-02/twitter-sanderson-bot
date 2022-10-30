from bs4 import BeautifulSoup
import requests
import time
import json

WEBSITE_ENDPOINT = 'https://www.brandonsanderson.com/'


def get_progress():
    project_status = {}
    html_text = requests.get(WEBSITE_ENDPOINT).text
    soup = BeautifulSoup(html_text, 'lxml')
    progress_bar = soup.find(
        'div', class_='vc_progress_bar wpb_content_element pb-style-three transparent-bg dt-style')
    projects = progress_bar.find_all('small', class_='vc_label')
    for project in projects:
        project_split = project.text.rsplit(' ', 1)
        project_status[project_split[0]] = project_split[1]
    return project_status


if __name__ == '__main__':
    sleep_seconds = 10
    while True:
        print(get_progress())
        time.sleep(sleep_seconds)
