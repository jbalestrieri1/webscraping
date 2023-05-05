import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

chapters = list(range(1,22))
random_chapter = random.choice(chapters)

if random_chapter < 10:
    url = 'https://ebible.org/asv/JHN'+ '0' + str(random_chapter) + '.htm'
else:
    url = 'https://ebible.org/asv/JHN'+ str(random_chapter) + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text)

#verses_list = soup.findAll('div', class_='p')
#verses_list = [ v.text.split('.') for v in verses_list ]
#print(verses_list)

page_verses = soup.findAll('div', class_='main')

for verses in page_verses:
    verses_list = verses.text.split(".")

mychoice = random.choice(verses_list[:-5])

verse = f'Chapter: {random_chapter} Verse: {mychoice}'

print(verse)

import keys
from twilio.rest import Client

client = Client(keys.accountSID, keys.auth_token)

TwilioNumber = ' '

mycellphone = ' '

textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber, body=verse)

