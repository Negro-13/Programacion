import pyperclip
import requests
from bs4 import BeautifulSoup

url = ''
while True:
    burl = pyperclip.paste()
    if burl != url:
        response = requests.get(burl)
        response.raise_for_status()
        html_file = open('./hoja/Web1.html', 'wb')
        for chunk in response.iter_content(10000):
            html_file.write(chunk)
        url = burl

        html_file = open('./hoja/Web1.html', 'r', encoding='utf-8')
        soup = BeautifulSoup(html_file, 'html.parser')

        print(f'Link de pagina: ' + burl)
        for p in soup.find_all('p'):
            print(p.get_text())