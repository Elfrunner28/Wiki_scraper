import requests
from bs4 import BeautifulSoup
import random

#requests wiki webpage, BS takes all the content from the request and runs a parser which makes the HTML look pretty, and next line identifies an id. then 

def scrape_wiki(url):
    response = requests.get(url=url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id='firstHeading')
    allLinks = soup.find(id='bodyContent').find_all('a')
    random.shuffle(allLinks)
    linkToScrape = 0    
    for link in allLinks:
        if link['href'].find("/wiki/") == -1: #-1 means that it was not found, which will stop current iteration and move to next. 
            continue
        if link['href'] == False:
            continue
        linkToScrape = link['href']
        break
    return linkToScrape  

def main():
    start_url = 'https://en.wikipedia.org/wiki/Lionel_Messi'
    un_url = scrape_wiki(start_url)
    url = 'https://en.wikipedia.org' + un_url
    x = 0
    while x < 50:
        print(scrape_wiki(url))
        x += 1
    
main()
