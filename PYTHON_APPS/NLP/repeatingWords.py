text = ''
url = ''

import requests
import url
import re 


def url_reader(input):
    #checking response

    response = requests.get(input)
    if response == 200:
        text_data = response.text
        return text_data
    else:
        text_data = response.status_code
        return  text_data




def repeating_words(text,url):

    with open(text,"r") as file:
    book = file.read()
    pattern  = re.compile("[a-zA-z]+")
    findings = re.findall(pattern,book.lower())  
    repeating_words = {}    
    for word in findings:
        if word in repeating_words.keys():
            repeating_words[word] =  repeating_words[word] + 1
        else:
            repeating_words[word] = 1 
    repeating_words = [(value,key) for (key,value) in repeating_words.items()]