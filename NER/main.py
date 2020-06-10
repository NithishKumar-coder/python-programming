import NER   #create NER module 
import sys
import json
def com(url):
    if "http" in url:
        NER.send(url)         
    else:
        print("Enter vaild url")
#get input from argv1
com(sys.argv[1])


##if you are running this code in vscode then,python main.py "the url you want to enter"
