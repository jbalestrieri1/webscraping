# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

table_rows = soup.findAll("tr")

state_death_ratio = ""
state_best_test = ""
state_worst_test = ""
high_death_ratio = 0.0
high_test_ratio = 0.0
low_test_ratio = 100.0


for row in table_rows[2:52]:
    td = row.findAll('td')
    state = td[1].text.strip('\n').strip('\n')
    cases = int(td[2].text.replace(",",""))
    death = int(td[4].text.replace(",",""))
    tested = int(td[10].text.replace(",",""))
    population = int(td[12].text.replace(",",""))

    death_ratio = death/cases
    test_ratio = tested/population

    if death_ratio > high_death_ratio:
        state_death_ratio = state
        high_death_ratio = death_ratio

    if test_ratio > high_test_ratio:
        state_worst_test = state
        high_test_ratio = test_ratio
    
    if test_ratio < low_test_ratio:
        state_best_test = state
        low_test_ratio = test_ratio

print(f"State with the highest death ratio is: {state_death_ratio}")
print(f"Death Ratio: {high_death_ratio:.2%}\n")
print(f"State with the best testing ratio is: {state_best_test}")
print(f"Test Ratio: {high_test_ratio:.2%}\n\n")
print(f"State with the worst testing ratio is: {state_worst_test}")
print(f"Test Ratio: {low_test_ratio:.2%}") 

