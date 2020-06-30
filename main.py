
import nltk

def findrelations(text):
    sentences = nltk.sent_tokenize(text)# разбить текст на предложения
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences] # разбить предложения на токены
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]# морфологический разбор
    chunked_sentences = nltk.ne_chunk_sents(tagged_sentences)#выделение именованных сущностей

    for doc in chunked_sentences:
        doc.draw()

text= open("test.txt", 'r', encoding='utf-8').read() #открыть файл русскоязычный файл
#text= open("test2.txt").read() #открыть файл англоязычный файл
findrelations(text)
