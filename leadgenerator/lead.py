import urllib.request
import re
import logging
import json
import csv
import help
from help import helper
from about_details import about_list
from bs4 import BeautifulSoup

#for extracting webpage
def get_webpage(url):
    try:
        response = urllib.request.Request(url, headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
        html = urllib.request.urlopen(response)
        html_bytes = html.read()
        page_html= html_bytes.decode("utf8")
        return page_html
        
    except:
        return None

#for getting text from webpage
def get_webpage_text(html):
    soup=BeautifulSoup(html,'lxml')
    content_text=soup.text  
    return content_text

#for getting list of companies and their contact links
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

#for getting exact contact page
def get_contact_page_link(html):
    rock=[]
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup.find_all('a'):
        try:
            if tag.has_attr('href'):
                link_ab=tag.attrs['href']           
                title=["Offices","about","contact","locations"]
                for item in title:
                    if item in link_ab:
                        rock.append(link_ab)
        except:
            link_ab=tag.get('href')
            if len(link_ab)!=0:
                title=["Offices","about","contact","locations"]
                for item in title:
                    if item in link_ab:
                        rock.append(link_ab)
    rock=list(dict.fromkeys(rock))
    return rock

#for getting us location
def get_location(text):
    rockers=help.helper(text)
    return rockers

#saaving as a json
def save_to_json(filename,json_dict):
     with open(filename, "w") as f:
        f.write(json.dumps(json_dict, sort_keys=False, indent=2, separators=(',', ': ')))
     return None
#coverting to csv
def json_to_csv_file(json_filename,csv_filename):
    with open(json_filename) as json_file: 
        data =json.load(json_file)
        temp=[]
        for i in data:
            temp.append({"company name":i,"location":data[i]})
        fields = ["company name","location"]  
        with open(csv_filename, 'w') as csvfile: 
            writer = csv.DictWriter(csvfile, fieldnames = fields, delimiter=',')  
            writer.writeheader()  
            writer.writerows(temp) 
    return None


if __name__=='__main__':
    invalid_html=[]
    #Create  logger
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
    print("\n")
    print("number of companies whose address we need to find is:",len(compa_list))
    address=[]
    for company in compa_list:
        complete=[]
        url=company[1]
        page_html=get_webpage(url)
        if page_html==None:
            print("can't access contact page of:"+company[0]+'\n')
            invalid_html.append(company[1])
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

    print("contact links and theeir respective companies\n\n")
    print(complete)
    print("companies with some issues:\n")
    print("\t",invalid_html)
    empty=[]        
    filename="new.json"
    com_dict={}
    for company in about_list:
        name=company[0]
        url=company[1]
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
                print("Address list:\n")
                print(loction_list)
                print('\n')
    
    print("\n companies and their respective addressess\n")
    print(com_dict)

    save_to_json(filename,com_dict)
    json_to_csv_file(filename,"new.csv")


