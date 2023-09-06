from bs4 import BeautifulSoup
import re #regular expressions module
import urllib2 #alternative to the request library for  downloading files from the internet
import os

#download params
image_type='Project'
movie='Avatar'
url='https://www.google.com/search?q='+movie+'&source=lnms&tbm=isch'

#creating soup with  url params and appropiate headers
header={'User-Agent':'Mozilla/5.0'}
soup=BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)))

