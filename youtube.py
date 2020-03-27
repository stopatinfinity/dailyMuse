import urllib.request
from bs4 import BeautifulSoup

def getSong(songs):
    query = urllib.parse.quote(songs)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    list = []

    for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
        list.append('https://www.youtube.com' + vid['href'])

    return list