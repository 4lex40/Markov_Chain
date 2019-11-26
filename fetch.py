import urllib.request
from bs4 import BeautifulSoup

def get_data():
    site = input('Enter lyrics url here(azlyrrics): ')
    site = "https://www.azlyrics.com/lyrics/joshgroban/pureimagination.html"
    page = urllib.request.urlopen(site)
    html_doc = page.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    a = soup.find_all('div')
    i = 0
    index = 0
    for div in a:
        str1 = str(div)
        if str1.find("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->") == -1:
            pass
        else:
            index = i
        i+=1
    str2 = str(a[index]).replace('<br/>',' ')
    print(str2)