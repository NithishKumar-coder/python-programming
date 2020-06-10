import re
#import urllib.request
from urllib.request import Request, urlopen  
from bs4 import BeautifulSoup
import spacy
import json
# create Entity module
import Entity
nlp =spacy.load('en_core_web_sm') 

Label_list=["DATE","PERSON","NORP","FAC","ORG","LOC","PRODUCT","EVENT","WORK_OF_ART","LAW","LANGUAGE","TIME","PERCENT","MONEY","QUALITY","ORDINAL","CARDINAL","GPE"]

def ner(url):
    # Getting the webpage
    req = Request(url, headers={'User-Agent': 'XYZ/3.0'})

    # Extracting the source code of the page.
    html = urlopen(req, timeout=10).read()
    
    # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
    soup = BeautifulSoup(html,"lxml")
    data = soup.findAll(text=True)
    
    def visible(element):
        #including elements in style,script,head 
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
        #for returning texts
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True
    result =list(filter(visible, data)) #The filter() function returns  text were the items are filtered through visible() function to test if the item is accepted or not.
    #replacing all \n characters obtained in result
    content_text=("".join(result)).replace("\n"," ")
    data_list=[]
    doc = nlp(content_text)
    for ent in doc.ents: 
        data_list.append({"Name":ent.text,"Entity":ent.label_})
    with open("Data.json", "w") as f:
            f.write(json.dumps(data_list, sort_keys=False, indent=2, separators=(',', ': '))) 
def send(web):
    ner(web)   
for label in Label_list:
    Entity.Get_Entity(label)
