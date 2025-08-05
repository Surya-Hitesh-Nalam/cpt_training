# 1. check if the string are octal strings using regex 
import re

def octal_str():
    l=eval(input())
    for s in l:
        pattern = r'^[0-7]{,3}+$'
        if re.match(pattern,s):
            print(f"{s} Octal string")
        else:
            print("Not octal string")
#octal_str()

#2. extarcting userid,domain,suffix from a email
import re

def extract_email():
    l=eval(input())
    for s in l:
        pattern = r'(\w+)@(\w+)\.(\w+)'
        match = re.match(pattern,s)
        if match:
            print(match.group(1),match.group(2),match.group(3))
        else:
            print("Not a valid email")
#extract_email()


'''3. split the irregular sentence to proper sentence

"Hi. How are you? I am fine. I am fine. I am fine. I am fine. I am fine."'''

import re

def split_sentence():
    l=eval(input())
    for s in l:
        pattern = r'\s[A-Z]'
        res = re.split(pattern,s)
        print(res)
#split_sentence()

#4th 

import re
tweet = """Gnd advice! RT @TheNestleb: what I would do differently if I was learning to code today
http://t.co/lwe jоркой ск: @gayherhardt Brstats"""
def clean_tweet(tweet):
    tweet = re.sub(r'(RT|CC)\s*@\w+:?', '', tweet)        
    tweet = re.sub(r'http\S+', '', tweet)                 
    tweet = re.sub(r'@\w+', '', tweet)                    
    tweet = re.sub(r'[^A-Za-z\s]', '', tweet)             
    tweet = re.sub(r'\s+', ' ', tweet)                   
    return tweet.strip()


#print(clean_tweet(tweet))


#5th code

import requests
import re

url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"
response = requests.get(url)
html = response.text

text_parts = re.findall(r'>([^<>]+)<', html)
cleaned_parts = [text.strip() for text in text_parts if text.strip()]

print(cleaned_parts)

#6th code
def start_end_same_char():
    words = eval(input("Enter list of words"))
    pattern = re.compile(r"^([a-zA-Z]).*\1$")
    matched_words = [word for word in words if pattern.match(word)]
    print(matched_words)