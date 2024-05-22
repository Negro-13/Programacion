import webbrowser, requests

data = requests.get('https://www.gutenberg.org/cache/epub/1112/pg1112.txt')

data.raise_for_status()

string = data.text[:100]

file = open('romeo.txt', 'w')
for chunk in string:
    file.write(chunk)
