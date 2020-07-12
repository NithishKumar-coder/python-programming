import requests 
import spacy
import re
import logging
import json
import csv
from bs4 import BeautifulSoup
url="http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.htm"   
nlp =spacy.load('en_core_web_sm') 
def get_webpage(url):
    if "http" in url:
        res=requests.get(url,headers={'User-Agent': 'XYZ/3.0'},timeout=5)
        data=res.text

        return data
    else:
        print("none")

def get_webpage_text(data):
    response=requests.get(data)
    html=response.text
    soup=BeautifulSoup(html,"lxml")
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
    #print(company_lists)
    
    return company_lists

def get_contact_page_link(html):
    rock=[]
    prefun=get_list(html)
    cena=[]
    for i in prefun[:2]:
        try:
            comp_name=i[0]
            comp_url=i[1]
            response=requests.get(comp_url)
            data=response.text
            beauty=BeautifulSoup(data,"lxml")
            link=beauty.findAll('a')
            for j in link:
                if "About" in j.text:
                    url=j.get('href')
                    if "http" in url:
                        rock.append([comp_name,url])
                    else:
                        rock.append([comp_name,comp_url+url])
        except:           
            logging.basicConfig(filename='company.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s',level=logging.INFO)
            logging.info(comp_name)
    for i in rock:
        if j not in cena:
            cena.append(i)
    return cena


def get_location(text):
    gets_list=[]
    doc=nlp(text)
    for ent in doc.ents:
        if 'GPE' in ent.label_:
            gets_list.append(ent.text)
    fresh=[]
    for i in gets_list:
        if i not in fresh:
            fresh.append(i)
    return fresh

def save_to_json(filename,json_dict):
     with open(filename, "w") as f:
            f.write(json.dumps(json_dict, sort_keys=False, indent=2, separators=(',', ': ')))

def json_to_csv_file(json_filename,csv_filename):
    with open(json_filename) as json_file: 
        data =json.load(json_file)
        temp=[]
        for i in data:
            temp.append({"company name":i,"location":data[i]})
        fields = ["company name","location"]  
        with open(csv_filename, 'w') as csvfile: 
            writer = csv.DictWriter(csvfile, fieldnames = fields)  
            writer.writeheader()  
            writer.writerows(temp) 


if __name__=='__main__':

    html= get_webpage(url)
    compa=get_list(html)
    print(compa)
    page_html=get_webpage(url)

    contact_list=get_contact_page_link(page_html)
    print(contact_list)
    print()
    filename="new.json"
    com_dict={}
    for company in contact_list:
        name=company[0]
        url=company[1]
        text=get_webpage_text(url)
        loction_list=get_location(text)
        loction_list.sort()
        com_dict[name]=loction_list
        print()
    print(com_dict)
    save_to_json(filename,com_dict)
    json_to_csv_file(filename,"new.csv")


