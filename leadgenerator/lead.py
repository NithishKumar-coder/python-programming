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
def get_list(page_html):
    soup=BeautifulSoup(page_html,"lxml")
    tab=soup.findAll("a",{"class":"100link"})
    company_lists=[]
    
    for i in tab:
        if i.text!="View From The Top Profile":
            company=[]
            company.append(i.text)
            company.append(i.get('href'))
            company_lists.append(company)
    return(company_lists)
def main():
    get_webpage(url)
main()


