import urllib.request
from newspaper import Article
import re
import logging
import json
import csv
import help

from bs4 import BeautifulSoup


def get_webpage(url):
    try:
        response = urllib.request.Request(url, headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
        html = urllib.request.urlopen(response)
        html_bytes = html.read()
        page_html= html_bytes.decode("utf8")
        return page_html
        
    except:
        return None

def get_webpage_text(html):
    soup=BeautifulSoup(html,'lxml')
    content_text=soup.text
    '''def visible(element):
            #including elements in style,script,head 
        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
            return False
            #for returning texts
        elif re.match('<!--.*-->', str(element.encode('utf-8'))):
            return False
        return True
    result =list(filter(visible, text)) #The filter() function returns  text were the items are filtered through visible() function to test if the item is accepted or not.
        #replacing all \n characters obtained in result
    content_text=("".join(result)).replace("\n"," ")  '''     
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
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup.find_all('a'):
        try:
            link_ab=tag.attrs['href']
            name=tag.text
            title=["Contact","Offices","about","contact","support"]
            for item in title:
                if item in name:
                    rock.append(link_ab)
        except:
            link_ab=tag.get('href')
            name=tag.text
            title=["Contact","Offices","about","contact","support"]
            for item in title:
                if item in name:
                    rock.append(link_ab)
    rock=list(dict.fromkeys(rock))
    return rock


def get_location(text):
    local_list=[]
    address=help.helper(text)
    for i in address:
        if i not in local_list:
            local_list.append(i)
    return local_list


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
    #Create and configure logger
    logging.basicConfig(filename="Company_details.log",format='%(asctime)s %(message)s',filemode='w')
    #Creating an object
    logger=logging.getLogger()
    #Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)
    logger.info("List of companies that has no contact details and no address details")

    url="http://www.econtentmag.com/Articles/Editorial/Feature/The-Top-100-Companies-in-the-Digital-Content-Industry-The-2016-2017-EContent-100-114156.htm"   

    html= get_webpage(url)
    compa_list=get_list(html)
    print(compa_list)

    address=[]
    for company in compa_list[:10]:
        complete=[]
        url=company[1]
        page_html=get_webpage(url)
        if page_html==None:
            print("can't access contact page of:"+company[0]+'\n')
            pass
        else:
            contact_list=get_contact_page_link(page_html)
            if len(contact_list):
                for i in contact_list:
                    if i.startswith('/'):
                        complete.append(company[1]+i)
                    else:
                        complete.append(i)
                address.append([company[0],complete])
            else:
               print("no location details available for"+company[0]+'\n')
               logger.setLevel(logging.DEBUG)
               logger.info("Sorry! no details are available")
               logger.info(company[0]) 

    empty=[]        
    filename="new.json"
    com_dict={}
    for company in address:
        name=company[0]
        url=company[1][0]
        urll=get_webpage(url)
        
        if urll==None:
            empty.append(name)
            pass
        else:
            text=get_webpage_text(urll)
            loction_list=get_location(text)
            if len(loction_list):
                com_dict.update({name:loction_list})
                print("Company_Name:",name)
                print("Addressess:",loction_list)
                print('\n')
            else:
                empty.append(name)
    
    print("\n companies and their respective addressess\n")
    print(com_dict)
    print("\n companies with no address")
    print(empty)
    for i in empty:
        logger.setLevel(logging.DEBUG)
        logger.info(i)

    save_to_json(filename,com_dict)
    json_to_csv_file(filename,"new.csv")


