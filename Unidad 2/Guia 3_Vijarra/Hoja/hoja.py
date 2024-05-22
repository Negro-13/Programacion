import pyperclip
from requests import get
from bs4 import BeautifulSoup

aurl = ""
while True:
    url = pyperclip.paste()
    if url != aurl:
        data = get(url)
        if data.status_code == 200:
            soup = BeautifulSoup(data.content, 'html.parser')
            parrafo = [p.get_text() for p in soup.find_all('p')]
            print(parrafo)
            aurl = url
        else:
            print("URL inválida.")