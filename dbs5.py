# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 18:01:28 2017

@author: Acedon
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 15:50:23 2017

@author: Acedon
"""

# imports
from bs4 import BeautifulSoup
import requests

# this function returns a soup page object ; Eiskalt aus dem beispiel übernommen
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

def main():
    #Das Https Thema auf heis.de hat 4 seiten, also 4 urls
    url1 = "https://www.heise.de/thema/https"
    url2 = "https://www.heise.de/thema/https?seite=1"
    url3 = "https://www.heise.de/thema/https?seite=2"
    url4 = "https://www.heise.de/thema/https?seite=3"
    
    splitarticle1 = getHeaders(url1)
    splitarticle2 = getHeaders(url2)
    splitarticle3 = getHeaders(url3)
    splitarticle4 = getHeaders(url4)
    
    #Zusammenfügen zu einer großen Überschriftenliste
    
    completesplit = splitarticle1 + splitarticle2 + splitarticle3 + splitarticle4
    complete = []
    for i in range(len(completesplit)):
        for j in range(len(completesplit[i])):
            complete.append(completesplit[i][j])
    
    top1 = ""
    top2 = ""
    top3 = ""
    top1c = 0
    top2c = 0
    top3c = 0
    
    # zählen der Wörter und merken der Top 3, meist genutzen Worte in Überschriften
    
    for i in range(len(complete)):
        test = complete[i]
        testc = 0
        for j in range(len(complete)):
            if (test == complete[j]):
                testc += 1
        if(testc > top1c):
            top1 = test
            top1c = testc
        if((testc > top2c) & (test != top1)):
            top2 = test
            top2c = testc
        if((testc > top3c) & (test != top1) & (test != top2)):
            top3 = test
            top3c = testc

    print("Top 1:",top1,"mit",top1c,"Vorkommen")
    print("Top 2:",top2,"mit",top2c,"Vorkommen")
    print("Top 3:",top3,"mit",top3c,"Vorkommen")
    
def getHeaders(url):
    data = getPage(url)    
    g_data = data.find_all("div",{"class":"recommendation"}) # finden der Überschriften
    article = []
    for item in g_data:
        article.append(item.header.text) # speicher der Überschriften als strings in eine Liste 
    splitarticle = []
    # Umwandeln der wahllos hinzugefügten Strings in Elemente einer Liste von Listen
    while article:
        splitarticle.append((article.pop(0)).split())
    return splitarticle


    
    
if __name__ == '__main__':
   main()