import requests
import codecs
from bs4 import BeautifulSoup


def get_url_for_searcg_vacancy():
    url = 'https://spb.hh.ru/search/vacancy/advanced?hhtmFrom=main'
    headers = {
        "User-Agent": "Your User Agent",  # Replace with your User-Agent header
    }


    resp = requests.get(url, headers=headers)


    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('form')














def find_work():
    erros = []
    jobs = []

    url = 'https://spb.hh.ru/search/vacancy?text=python'

    headers = {
        "User-Agent": "Your User Agent",  # Replace with your User-Agent header
    }

    resp = requests.get(url, headers=headers)

    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, 'html.parser')
        main_div = soup.find('div', id='a11y-main-content')

        if main_div:
            div_list = main_div.find_all(
                'div', class_='vacancy-serp-item__layout')

            for div in div_list:

                title = div.find('h3')
                link = title.a['href']
                company = div.find('div', class_='bloko-text').text
                title_vacancy = div.find(
                    'span', class_='serp-item__title').text
                description = 'Data not found'
                jobs.append({'url': link, 'title': title_vacancy,
                            'company': company, 'description': description})
        else:
            erros.append({'url': url, 'title': 'Div not exist'})

    else:
        erros.append({'url': url, 'title': 'Page not response'})


if __name__ == '__main__':
    with open('result.html',  mode='w', encoding='utf-8') as file:
        file.write(str(jobs))
