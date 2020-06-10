# NAMED ENTITY RECOGNIZER
       A simple  project determining the entity of words using Python.



# Getting Started
     The main idea behind or project is we need to check the entity with spacy module and to categorize each entity based on its type.

## Technologies

    Project is created with:
    Python-3.8.3
    visual studio code


## Prerequisites

	To run this project, we need to install:
	requests-2.23.0 
	spacy
	json

## requests-2.23.0

	requests can be installed by pip in windows terminal
	      ~pip install requests
	      ##it is used to send HTTP requests and get response object.


## spacy

	it can be obtained by
		~pip install spacy
		## It is used for comparing the words with the entity.


# json

	it is an in-built module in python-3.6.3 and above so you don't need to install it 
	if you find any errors then use
		~pip install json5
		## it is used for storing different types of recognized entities.


## Launch

	steps to run the project :
python main.py  **arg1** 
Where **arg1** is a **URL**  


	1.first arg1 given by the user contains a webpage.

	2.it will initiate the web scraping process in NER.py,where the url is  get&extracted using requests&beautifulsoup4.

	3.then the process moves on to entity recognition. 
		it is done with the help of spacy module

	4.now the spacy module identify the types of entity.
	all these entities are stored in Data.json

	5.it will be produced as an output to the user.

	6. the obtained entities are collected and separeted according to their types in all_entities.json file.
