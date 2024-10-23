import requests
from bs4 import BeautifulSoup
import random 

def scrapeWiki(url):
    page = requests.get(
        url=url
    )
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='firstHeading')
    print(title.string)
    
    all_links = soup.find(id='bodyContent').find_all('a')
    random.shuffle(all_links)
    scraped_link = 0
    
    for link in all_links:
        if link['href'].find('/wiki/') == -1:
            continue
    
        scraped_link = link
        break
    scrapeWiki('https://en.wikipedia.org' + scraped_link['href'])
    
scrapeWiki('https://en.wikipedia.org/wiki/Warhammer_40,000')