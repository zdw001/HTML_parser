from bs4 import BeautifulSoup
from datetime import datetime
import winsound
import requests
import time
import functions
import webbrowser
import threading
import textwrap  # for cutting length in idle window
from threading import Timer
import os
import mouse_click

# sound feature
Freq = 1300
Dur = 500

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
explorer = 'c:\\program files (x86)\\internet explorer\\iexplore.exe'


class scraper:
    def __init__(self, url, tag, tag2, occurence, who, open_browser, keyword_list, citron, soup_type):
        self.url = url
        self.tag = tag
        self.tag2 = tag2
        self.occurence = occurence
        self.who = who
        self.open_browser = open_browser
        self.keyword_list = keyword_list
        self.citron = citron
        self.soup_type = soup_type

    def getSite(self):
        old_array = []
        body_array = [] 

        while True:
            if self.url == "https://ptab.uspto.gov/ptabe2e/rest/petitions/1461718/documents?availability=PUBLIC&cacheFix=" or self.url == "https://ptab.uspto.gov/ptabe2e/rest/petitions/1463994/documents?availability=PUBLIC&cacheFix=":
                headline = requests.get(self.url, headers=headers)
                soup = BeautifulSoup(headline.content, self.soup_type).text
                title = soup[1000:2000]
                old_array = [title]
                print("ptab received")
            else:
                try:
                    headline = requests.get(self.url, headers=headers)
                    soup = BeautifulSoup(headline.content, self.soup_type)
                    if self.tag != "href":
                        title = soup.find_all(self.tag)[self.occurence].text
                    #citron specific, else enter None
                    if self.citron != None:
                        body = soup.find_all("description")[1].text
                        citron = functions.find_citron_ticker(body)
                    #Ny post specific, else enter None
                    if self.keyword_list != None:
                        body_soup = BeautifulSoup(headline.content, "html.parser")
                        body = body_soup.find_all("description")[1].text
                    #bronte conditional
                    if self.tag == "href":
                        title = soup.find_all("a", href = True)[self.occurence].text
                    output = [self.who + ":", title]
                    print(self.who + ' received')
                    old_array = [output[1]]
                except IndexError:
                    print(self.who + ' initialization error')
                    print(self.who)
                    continue
            break

        while True:
            if self.url == "https://ptab.uspto.gov/ptabe2e/rest/petitions/1461718/documents?availability=PUBLIC&cacheFix=" or self.url == "https://ptab.uspto.gov/ptabe2e/rest/petitions/1463994/documents?availability=PUBLIC&cacheFix=":
                request = requests.get(self.url, headers=headers)
                soup = BeautifulSoup(request.content, self.soup_type).text
            else:
                try:
                    request = requests.get(self.url, headers=headers)
                except:
                    print(self.who + " blocked you!")
                soup = BeautifulSoup(request.content, self.soup_type)
            if self.keyword_list == None:
                try:
                    if self.tag == "ptab":
                        new = soup[1000:2000]
                    if self.tag == "href":
                        new = soup.find_all("a", href = True)[self.occurence].text
                    if self.tag != "ptab" and self.tag != "href":
                        new = soup.find_all(self.tag)[self.occurence].text
                    #bronte conditional
                    
                except IndexError:
                    new = old_array[-1]
                    print(self.who + ' error')
                    print(datetime.now())
                    time.sleep(1)
                    print("\n")
                    time.sleep(1)
                    print("\n")
                    time.sleep(1)
                    print("\n")
                    time.sleep(1)
                    print("\n")
                if functions.check_change(old_array, new) == True:
                    short_title = textwrap.wrap(new, 60)
                    print("\n-------------------------------------------------------------\n" + self.who + ":")
                    #citron conditional
                    if self.citron != None:
                        body = soup.find_all("description")[1].text
                        citron = functions.find_citron_ticker(body)
                        print(citron)
                    for line in short_title:
                        print(line)
                    #kerrisdale conditional
                    if self.tag2 != None:
                        tag_two = soup.find_all(self.tag2)[1].text
                        print(tag_two)
                    print(datetime.now())
                    old_array.append(new)
                    winsound.Beep(Freq, Dur)
                    functions.open_browser(self.open_browser)
                    time.sleep(30)
                    if len(old_array) > 5:
                        del old_array[0]
            #nypost conditional
            if self.keyword_list != None:
                try:
                    new = soup.find_all(self.tag)[self.occurence].text
                    body = BeautifulSoup(request.content, "html.parser").find_all("description")[1].text
                except IndexError:
                    print(self.who)
                    new = old_array[-1]
                    body = body_array[-1]
                if functions.check_change(old_array, new) == True:
                    if functions.nypost_keyword(new, body, self.keyword_list) == True:
                        short_title = textwrap.wrap(new, 60)
                        for line in short_title:
                            print(line)
                        old_array.append(new)
                        body_array.append(body)
                        winsound.Beep(Freq, Dur)
                        functions.open_browser(self.open_browser)
                        time.sleep(30)
                        if len(old_array) > 5:
                            del old_array[0]
                        if len(body_array) > 5:
                            del body_array[0]
            time.sleep(.5)
                            

# url, tag, tag2, occurence, who, open_browser, keywords, citron, soup type
aurelius = scraper("http://aureliusvalue.com/feed", "title", None, 1, "Aurelius", "http://www.aureliusvalue.com", None, None, "lxml")
citron = scraper("http://citronresearch.com/feed", "title", None, 1, "Citron", "http://citronresearch.com/", None, True, "lxml")
gotham = scraper("http://gothamcityresearch.com/research/feed", "title", None, 3, "Gotham City",
                 "https://gothamcityresearch.com/research", None, None, "lxml")
nypost = scraper("http://nypost.com/feed", "title", None, 2, "NY Post", "http://nypost.com/feed", ["to merge", "approval",
                          "merger", "for", "acquisition","federal trade commision", "terminate","buyout", "up for sale",
                          "in talks to buy", "doj", "sources told the post", "ftc", "source", "department of justice",
                            "the post has learned", "pe firm", "pe"], None, "lxml")
sirf = scraper("http://sirf-online.org/feed", "title", None, 1, "SIRF", "http://sirf-online.org/", None, None, "lxml")
prescience = scraper("http://presciencepoint.com/research/feed", "title", None, 1, "Prescience Point",
                     "http://www.presciencepoint.com/research", None, None, "lxml")
kerrisdale = scraper("https://www.kerrisdalecap.com", "h2", "p", 1, "Kerrisdale", "https://www.kerrisdalecap.com", None, None, "lxml")
sprucepoint = scraper("http://sprucepointcap.com/feed/", "title", None, 1, "Spruce Point", "http://sprucepointcap.com", None, True, "html.parser")
muddywaters = scraper("http://www.muddywatersresearch.com/feed/?post_type=reports", "title", None, 1, "Muddy Waters", "http://muddywatersresearch.com/research", None, None, "lxml")
brontecap = scraper("http://brontecapital.blogspot.com/", "href", None, 0, "Bronte Cap", "http://brontecapital.blogspot.com/", None, None, "lxml")
lly1 = scraper("https://ptab.uspto.gov/ptabe2e/rest/petitions/1461718/documents?availability=PUBLIC&cacheFix=", "ptab", None, 0, "LLY IPR", "https://ptab.uspto.gov/ptabe2e/rest/petitions/1461718/documents?availability=PUBLIC&cacheFix=", None, None, "lxml")
lly2 = scraper("https://ptab.uspto.gov/ptabe2e/rest/petitions/1463994/documents?availability=PUBLIC&cacheFix=","ptab", None, 0, "LLY IPR", "https://ptab.uspto.gov/ptabe2e/rest/petitions/1461718/documents?availability=PUBLIC&cacheFix=", None, None, "lxml")
betaville = scraper("https://www.betaville.co.uk/", "href", None, 7, "Betaville","https://www.betaville.co.uk/", ["rare alert"], None, "lxml")               

site_list = [citron, gotham, nypost, sirf, prescience, sprucepoint, muddywaters, brontecap, lly1, lly2]
    

def run_scraper(site_list):
    for site in site_list:
        thread = threading.Thread(target=site.getSite)
        thread.start()
    click = threading.Thread(target=mouse_click.refresh_cnbc(3000))
    click.start()


    

