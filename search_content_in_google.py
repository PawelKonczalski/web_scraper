from bs4 import BeautifulSoup
import requests

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}

search = input('Enter search phrase: ')
search = search.replace(' ', '+')
params = {'q': search}

r = requests.get('https://www.google.com/search', params, headers=headers)

soup = BeautifulSoup(r.content, "html.parser")
for g in soup.findAll('div', {'class': 'r'}):
    result = g.findAll('a')
    if result:
        title = g.find('h3').text
        link = result[0]['href']
        print(title)
        print(link)
        print(g.parent.find('span', {'class': 'st'}).text)
        print()



