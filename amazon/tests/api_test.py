import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://www.amazon.com/')

soup = bs.BeautifulSoup(source,'lxml')





