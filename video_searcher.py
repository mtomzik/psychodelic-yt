import urllib
import urllib2
from bs4 import BeautifulSoup

textToSearch = 'psychedelic weird videos'
query = urllib.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, "lxml")
urls = []
for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
    urls.append('https://www.youtube.com' + vid['href'])
for i in urls : 
	print i
print len(urls)