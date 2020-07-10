import requests 
import re
from bs4 import BeautifulSoup
url="http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.htm"   

def get_webpage(url):
    if "http" in url:
        res=requests.get(url)
        data=res.text
        get_webpage_text(data)

        get_contact_page_link(data)

        return data
    else:
        print("none")

def get_webpage_text(data):
    soup=BeautifulSoup(data,"lxml")
    text=soup.findAll(text=True)
    def visible(element):
        #including elements in style,script,head 
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        #for returning texts
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True
    result =list(filter(visible, text)) #The filter() function returns  text were the items are filtered through visible() function to test if the item is accepted or not.
    #replacing all \n characters obtained in result
    content_text=("".join(result)).replace("\n"," ")
    return content_text

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
    
    return company_lists

def get_contact_page_link(html):
    rock=[]
    prefun=get_list(html)
    l=[]
    
    for i in prefun:
        l.append(i[1])
    for j in l:
        response=requests.get(j, timeout=5)
        data=response.text
        beauty=BeautifulSoup(data,"lxml")
        link=beauty.findAll('a')
        for ij in link:
            if ij.text=="About" or ij.text=="Contact Us":
                rock.append(ij.get('href'))
        print(rock)


def main():
    get_webpage(url)
main()


