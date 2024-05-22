import requests
from bs4 import BeautifulSoup

url = 'https://www.estebanecheverria.gob.ar/galeria-imagenes/'  
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    images = soup.find_all('img')
    image_urls = []
    for img in images:
        img_src = img.get('src')
        if img_src:
            img_url = requests.compat.urljoin(url, img_src)
            image_urls.append(img_url)
    for img_url in image_urls:
        print(img_url)
else:
    print(f"Failed to retrieve the webpage: {response.status_code}")