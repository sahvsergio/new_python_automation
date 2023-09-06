import bs4
import requests
test_site=requests.get('https://www.savant-international.com/')
site_html=test_site.content

soup= bs4.BeautifulSoup(site_html,'lxml')
print(type(soup))
links=soup.find_all('a'[0])
print(links, sep='/n')

#Downloading_content_from_the_Web.py