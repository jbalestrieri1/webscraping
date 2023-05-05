import random 
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

webpage = 'https://biblehub.com/asv/john/1.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

verses_list = soup.findAll('p', class_='reg')

#for verse in verses_list:
#   print(verse.text)

verses_list = [ v.text.split('.') for v in verses_list ]

#print(verses_list)

print(random.choice(random.choice(verses_list)))
