import requests 
from bs4 import BeautifulSoup
url="http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.htm"   

def get_webpage(url):
    if "http" in url:
        res=requests.get(url)
        data=res.text
        get_webpage_text(data)
        return data
    else:
        print("none")

def get_webpage_text(data):
    soup=BeautifulSoup(data,"lxml")
    text=soup.findAll("p")
    print(text)
    return text
def main():
    get_webpage(url)
main()


