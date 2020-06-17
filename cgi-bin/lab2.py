#!/usr/bin/env python3

print("Content-type: text/html")

#print()

#print("<h1>Hello World! привет мир!</h1>")
import nltk

from nltk.tokenize import PunktSentenceTokenizer
from nltk.sem import extract_rels
import re
import cgi, cgitb 

# Создание экземпляра FieldStorage
form = cgi.FieldStorage() 

# Получение данных из полей
if form.getvalue('textcontent'):
   sample_text = form.getvalue('textcontent')
else:
   sample_text = "Иванов Иван работает в компании ОАО Крафтнефть с 2015 года в должности главного инженера"

custom_sent_tokenizer = PunktSentenceTokenizer()
tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
   try:
      for i in tokenized:
         words = nltk.word_tokenize(i)
         tagged = nltk.pos_tag(words)
         namedEnt = nltk.ne_chunk(tagged, binary=False)
         namedEnt.draw()

   except Exception as e:
      print(str(e))
process_content()
