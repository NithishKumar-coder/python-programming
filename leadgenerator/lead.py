from urllib.request import Request, urlopen  
from bs4 import BeautifulSoup

def main():
    url="http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.htm"   
    def get_webpage(url):
        # Getting the webpage
        req = Request(url, headers={'User-Agent': 'XYZ/3.0'})

        # Extracting the source code of the page.
        html = urlopen(req).read()
        return html
    

    
main()
