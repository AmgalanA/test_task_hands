from requests import Session
from bs4 import BeautifulSoup

base_url = 'https://repetitors.info/'

base_url_second = 'https://hands.ru/company/about/'

def main(base_url):
    s = Session()

    response = s.get(base_url)
    soup = BeautifulSoup(response.text, 'lxml')

    footer_cards = soup.find_all('footer')

    for card in footer_cards:
        text = card.text
        if len(text) > 0 and '8' in text:
            for index in range(len(text)):
                char = text[index]
                if char == '8':
                    # Print out the phone number
                    print(text[index:index+17])

    div_cards = soup.find_all('div')

    for card in div_cards:
        text = card.text
        if len(text) > 0 and '8()' in text:
            for index in range(len(text)):
                char = text[index]
                if char == '8':
                    # Print out the phone number
                    print(text[index:index+17])

main(base_url)
main(base_url_second)