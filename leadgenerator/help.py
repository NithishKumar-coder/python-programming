import usaddress
import re
def helper(text):
    address_list=[]
    li=[r'[0-9|a-zA-Z]*\s[a-z|A-Z|0-9]*\s[A-Z|a-z|0-9]*\s[A-Z|a-z|0-9]*[,]\s[A-Z]{2}[\s][0-9]{5}',r'[0-9|A-Z|a-z ]*\n[A-Z|a-z ]*\n\t\t\t\t\t[A-Z|a-z]*[,]\s[A-Z]{2}\s[0-9]{5}',r'[0-9|A-Z|a-z]*\s[A-Z|a-z|0-9]*\s[A-Z|a-z|0-9]*[, ]\s[A-Z|a-z]*\s[0-9]*\n[A-Z|a-z\s]*[,]\s[A-Z]{2}\s[0-9]{5}',r'^\s[0-9]{3}\s[a-z|A-Z|0-9\s]*[,]\s[0-9|a-z|A-Z]*\s[a-z|A-Z]*\n[A-Z|a-z\s]*[, ]\s[A-Z]{2}\s[0-9]{5}',r'^[0-9a-zA-Z ]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]{5}\n\bUnited States|USA\b$',r'^[0-9]{3}[a-z|A-Z\s]*\s[a-z|A-Z]{2}.[A-Z|a-z]*\s[0-9]*[A-z|a-z|0-9]*[,]\s[A-Z]{2}\s[0-9]{5}$']
    for element in li:
        find = re.findall(element,text.strip(), flags = re.MULTILINE)
        for item in find:
            item= re.sub(r'[^\x00-\x7f]',' ', item)
            item= re.sub(r'\n|\t|\r',' ', item)
            if len(item)>4:
                 address_list.append(item)
    address_list=list(dict.fromkeys(address_list))

    #parsing with usaddress module
    detail_list=[]
    for i in address_list:
        detail_list.append(usaddress.parse(i))
    l=[]
    for item in detail_list:
        details_dict={}
        for inner_item in item:
            details_dict[inner_item[1]]=inner_item[0]
        l.append(details_dict)
    return l
