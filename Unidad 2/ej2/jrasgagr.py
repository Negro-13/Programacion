import webbrowser, requests
from bs4 import BeautifulSoup
import os
data =requests.get('https://www.estebanecheverria.gob.ar/galeria-imagenes/')
data.raise_for_status()
soup=BeautifulSoup(data.text,'html.parser')

images = soup.find_all('imgs')
image_urls = []
for i in range(len(images)):
    image_urls.append(images[i].get('src'))
for url in image_urls:
    File = open(os.path.join('dirl', os.path.basename(img_src)), 'wb')
    File.write(url.content)