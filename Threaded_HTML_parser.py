from bs4 import BeautifulSoup
from datetime import datetime
import winsound
import requests
import time
import functions
import webbrowser
import threading
import textwrap #for cutting length in idle window
import os
from threading import Timer
import mouse_click
from  requests.exceptions import ConnectionError

##import colorama

#set a time to shut scraper off
x=datetime.today()
y=x.replace(day=x.day+1, hour=16, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

def quit_now():
    os.system("taskkill /f /im pythonw.exe")

t = Timer(secs, quit_now)
t.start()

#sound feature
Freq = 1300
Dur = 500

print("Initializing... \n")

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

aurelius_url = 'http://www.aureliusvalue.com/feed'
citron_url = 'http://www.citronresearch.com/feed'
gotham_url = 'http://gothamcityresearch.com/research/feed'
nypost_url = 'http://nypost.com/feed'
sirf_url = 'http://sirf-online.org/feed'
prescience_url =  'http://www.presciencepoint.com/research/feed'
sprucepoint_url = "http://www.sprucepointcap.com/feed"
muddy_url = "http://www.muddywatersresearch.com/feed/?post_type=reports"
bronte_url = "http://brontecapital.blogspot.com/"
betaville_url = "https://www.betaville.co.uk/"
##lly1_url = "https://ptab.uspto.gov/ptabe2e/rest/petitions/1461718/documents?availability=PUBLIC&cacheFix="
lly2_url = "https://ptab.uspto.gov/ptabe2e/rest/petitions/1463994/documents?availability=PUBLIC&cacheFix="

urls = [lly2_url, betaville_url, bronte_url, muddy_url, sprucepoint_url, aurelius_url, citron_url, gotham_url, nypost_url, sirf_url, prescience_url]

explorer = 'c:\\program files (x86)\\internet explorer\\iexplore.exe'

def getSite(url):

    aurelius_old_array = []
    citron_old_array = []
    gotham_old_array = []
    nypost_old_array = []
    nypost_body_array = []
    sirf_old_array = []
    prescience_old_array = []
    sprucepoint_old_array = []
    muddy_old_array = []
    bronte_old_array = []
    betaville_old_array = []
##    lly1_old_array = []
    lly2_old_array = []
    
    if url ==aurelius_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("title")[1].text
                aurelius =  ["Aurelius:", title]
                print('aurelius received')
                aurelius_old_array = [aurelius[1]]
            except IndexError:
                print("aurelius initialization error")
                continue
            break
    elif url ==citron_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("title")[2].text
                body = soup.find_all("description")[1].text
                ticker = functions.find_citron_ticker(body)
                citron =  ["Citron:", title, ticker]
                print('citron received')
                citron_old_array = [citron[1]]
            except IndexError:
                print("citron initialization error")
                continue
            break
    elif url ==gotham_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("title")[3].text
                gotham = ["Gotham:", title]
                print('gotham received')
                gotham_old_array = [gotham[1]]
            except IndexError:
                print("gotham initialization error")
                continue
            break
    elif url ==nypost_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("title")[2].text
                body_soup = BeautifulSoup(headline.content, "html.parser")
                body = body_soup.find_all("description")[1].text
                nypost = ["NY Post:", title, body]
                print('nypost received')
                nypost_old_array = [nypost[1]]
                nypost_body_array = [nypost[2]]
            except IndexError:
                print("nypost initialization error")
                continue
            break
    elif url ==sirf_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("title")[1].text
                sirf = ["SIRF:", title]
                print('sirf received')
                sirf_old_array = [sirf[1]]
            except IndexError:
                print("sirf initialization error")
                continue
            break
    elif url ==prescience_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("title")[1].text
                prescience = ["Prescience:", title]
                print('prescience received')
                prescience_old_array = [prescience[1]]
            except IndexError:
                print("prescience initialization error")
                continue
            break
    elif url == sprucepoint_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("title")[1].text
                sprucepoint =  ["sprucepoint:", title]
                print('Sprucepoint received')
                sprucepoint_old_array = [sprucepoint[1]]
            except IndexError:
                print("Sprucepoint initialization error")
                continue
            break
    elif url == muddy_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("title")[1].text
                muddy =  ["Muddywaters:", title]
                print('Muddywaters received')
                muddy_old_array = [muddy[1]]
            except IndexError:
                print("Muddywaters initialization error")
                continue
            break
    elif url == bronte_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("a", href= True)[0].text
                bronte =  ["Bronte:", title]
                print('Bronte received')
                bronte_old_array = [bronte[1]]
            except IndexError:
                print("Bronte initialization error")
                continue
            break
    elif url == betaville_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml")
                title = soup.find_all("a", href= True)[7].text
                betaville =  ["Betaville:", title]
                print('Betaville received')
                betaville_old_array = [betaville[1]]
            except IndexError:
                print("Betaville initialization error")
                continue
            break

    #PTAB
##    elif url == lly1_url:
##        while True:
##            try:
##                headline = requests.get(url, headers = headers)
##                soup = BeautifulSoup(headline.content, "lxml").text
##                title = soup[1000:2000]
##                lly1 =  ["LLY IPR:", title]
##                print('LLY IPR received')
##                lly1_old_array = [lly1[1]]
##            except IndexError:
##                print("LLY IPR initialization error")
##                continue
##            break
    elif url == lly2_url:
        while True:
            try:
                headline = requests.get(url, headers = headers)
                soup = BeautifulSoup(headline.content, "lxml").text
                title = soup[1000:2000]
                lly2 =  ["LLY IPR:", title]
                print('LLY IPR received')
                lly2_old_array = [lly2[1]]
            except IndexError:
                print("LLY IPR initialization error")
                continue
            break

    while True:
        request = requests.get(url, headers = headers)

        if url == aurelius_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                aurelius_new = soup.find_all("title")[1].text
            except IndexError:
                aurelius_new = aurelius_old_array[-1]
                print("aurelius Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("aurelius connection error")
            if functions.check_change(aurelius_old_array, aurelius_new) == True:
                aurelius_short_title = textwrap.wrap(aurelius_new, 60) #for idle interface
                print("\n------------------------------------------------------------------------------------\n" + "Aurelius Value:")
                for line in aurelius_short_title: #idle config
                    print(line) #print aurelius new for normal title
                aurelius_old_array.append(aurelius_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("http://www.aureliusvalue.com/")
                time.sleep(30) #delay half second
                if len(aurelius_old_array) > 5:
                    del aurelius_old_array[0]
            time.sleep(.5)
                
        elif url == citron_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                citron_new = soup.find_all("title")[2].text
                citron_body_new = soup.find_all("description")[1].text
            except IndexError:
                citron_new = citron_old_array[-1]
                print("Citron Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("citron connection error")
            citron_ticker = functions.find_citron_ticker(citron_body_new)
            if functions.check_change(citron_old_array, citron_new) == True:
                citron_short_title = textwrap.wrap(citron_new, 60) #for idle interface
                print("\n------------------------------------------------------------------------------------\n" + "Citron Research:")
                print(citron_ticker)
                for line in citron_short_title:
                    print(line)
                citron_old_array.append(citron_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("http://citronresearch.com/feed")
                time.sleep(30) #delay half second
                if len(citron_old_array) > 5:
                    del citron_old_array[0]
            time.sleep(.5)

        elif url == gotham_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                gotham_new = soup.find_all("title")[3].text
            except IndexError:
                gotham_new = gotham_old_array[-1]
                print("Gotham Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("gotham connection error")
            if functions.check_change(gotham_old_array, gotham_new) == True:
                gotham_short_title = textwrap.wrap(gotham_new, 60) #for idle interface
                print("\n------------------------------------------------------------------------------------\n" + "Gotham City Research:")
                for line in gotham_short_title:
                    print(line)
                gotham_old_array.append(gotham_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("https://gothamcityresearch.com/research/")
                time.sleep(30) #delay half second
                if len(gotham_old_array) > 5:
                    del gotham_old_array[0]
            time.sleep(.5)

        elif url == nypost_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                nypost_new = soup.find_all("title")[2].text
            except IndexError:
                nypost_new = nypost_old_array[-1]
                print("NYPost Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("nypost connection error")
            if functions.check_change(nypost_old_array, nypost_new) == True:
                nypost_old_array.append(nypost_new)
                try:
                    nypost_body = BeautifulSoup(request.content, "html.parser").find_all("description")[1].text
                except IndexError:
                    nypost_body = nypost_body_array[-1]
                if functions.nypost_keyword(nypost_new, nypost_body, ["exclusive","to merge", "approval",
                  "merger", "acquisition","federal trade commision", "terminate","buyout", "up for sale",
                  "in talks to buy", "doj", "ftc", "source", "department of justice",
                    "the post has learned", "pe firm", "pe"]) == True:
                    nypost_short_title = textwrap.wrap(nypost_new, 60) #for idle interface
                    for line in nypost_short_title:
                        print(line)
                    nypost_old_array.append(nypost_new)
                    nypost_body_array.append(nypost_body)
                    winsound.Beep(Freq, Dur)
                    webbrowser.open("http://nypost.com/feed")
                    time.sleep(30) #delay half second
                    if len(nypost_old_array) > 5:
                        del nypost_old_array[0]
                    if len(nypost_body_array) > 5:
                        del nypost_body_array[0]
            time.sleep(.5)
                
        elif url == sirf_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                sirf_new = soup.find_all("title")[1].text
            except IndexError:
                sirf_new = sirf_old_array[-1]
                print("SIRF Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("sirf connection error")
            if functions.check_change(sirf_old_array, sirf_new) == True:
                sirf_short_title = textwrap.wrap(sirf_new, 60) #for idle interface
                print("\n------------------------------------------------------------------------------------\n" + "SIRF:")
                
                for line in sirf_short_title:
                    print(line)
                sirf_old_array.append(sirf_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("http://sirf-online.org/")
                time.sleep(30) #delay half second
                if len(sirf_old_array) > 5:
                    del sirf_old_array[0]
            time.sleep(.5)

        elif url == prescience_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                prescience_new = soup.find_all("title")[1].text
            except IndexError:
                prescience_new = prescience_old_array[-1]
                print("Prescience Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("prescience connection error")
            if functions.check_change(prescience_old_array, prescience_new) == True:
                prescience_short_title = textwrap.wrap(prescience_new, 60) #for idle interface
                print("\n------------------------------------------------------------------------------------\n" + "Prescience Point:")
                for line in prescience_short_title:
                    print(line)
                prescience_old_array.append(prescience_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("http://www.presciencepoint.com/research/")
                time.sleep(30) #delay half second
                if len(prescience_old_array) > 5:
                    del prescience_old_array[0]
            time.sleep(.5)

        elif url == sprucepoint_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                sprucepoint_new = soup.find_all("title")[1].text
                sprucepoint_body_new = soup.find_all("description")[1].text
            except IndexError:
                sprucepoint_new = sprucepoint_old_array[-1]
                print("Sprucepoint Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("sprucepoint connection error")
            sprucepoint_ticker = functions.find_citron_ticker(sprucepoint_body_new)
            if functions.check_change(sprucepoint_old_array, sprucepoint_new) == True:
                sprucepoint_short_title = textwrap.wrap(sprucepoint_new, 60) #for idle interface
                print("\n------------------------------------------------------------------------------------\n" + "SprucePoint:")
                for line in sprucepoint_short_title:
                    print(line)
                print(citron_ticker)
                sprucepoint_old_array.append(sprucepoint_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("http://sprucepointcap.com")
                time.sleep(30) #delay half second
                if len(sprucepoint_old_array) > 5:
                    del sprucepoint_old_array[0]
            time.sleep(.5)

        elif url == muddy_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                muddy_new = soup.find_all("title")[1].text
            except IndexError:
                muddy_new = muddy_old_array[-1]
                print("MuddyWaters Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("muddy waters connection error")
            if functions.check_change(muddy_old_array, muddy_new) == True:
                muddy_short_title = textwrap.wrap(muddy_new, 60) #for idle interface
                print("\n------------------------------------------------------------------------------------\n" + "Muddy Waters:")
                for line in muddy_short_title:
                    print(line)
                muddy_old_array.append(muddy_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("http://muddywatersresearch.com/research")
                time.sleep(30) #delay half second
                if len(muddy_old_array) > 5:
                    del muddy_old_array[0]
##            time.sleep(.5)

        elif url == bronte_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                bronte_new = soup.find_all("a", href= True)[0].text
            except IndexError:
                bronte_new = bronte_old_array[-1]
                print("Bronte Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("bronte connection error")
            if functions.check_change(bronte_old_array, bronte_new) == True:
                bronte_short_title = textwrap.wrap(bronte_new, 60) #for idle interface
                print("\n------------------------------------------------------------------------------------\n" + "Bronte Cap:")
                for line in bronte_short_title:
                    print(line)
                bronte_old_array.append(bronte_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("http://brontecapital.blogspot.com/")
                time.sleep(30) #delay half second
                if len(bronte_old_array) > 5:
                    del bronte_old_array[0]
            time.sleep(.5)
                    
        elif url == betaville_url:
            try:
                soup = BeautifulSoup(request.content, "lxml")
                betaville_new = soup.find_all("a", href= True)[7].text
            except IndexError:
                betaville_new = betaville_old_array[-1]
                print("Betaville Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("betaville connection error")
            if functions.check_change(betaville_old_array, betaville_new) == True:
                betaville_short_title = textwrap.wrap(betaville_new, 60) #for idle interface
                print("\n------------------------------------------------------------------------------------\n" + "Betaville:")
                for line in betaville_short_title:
                    print(line)
                betaville_old_array.append(betaville_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("https://www.betaville.co.uk/")
                time.sleep(30) #delay half second
                if len(betaville_old_array) > 5:
                    del betaville_old_array[0]
            time.sleep(.5)

        #PTAB
##        elif url == lly1_url:
##            try:
##                soup = BeautifulSoup(request.content, "lxml").text
##                llyl_new = soup[1000:2000]
##            except IndexError:
##                lly1_new = lly1_old_array[-1]
##                print("LLY IPR Error")
##                time.sleep(1)
##                print("\n")
##                time.sleep(1)
##                print("\n")
##                time.sleep(1)
##                print("\n")
##                time.sleep(1)
##                print("\n")
##            except ConnectionError:
##                print("LLY IPR connection error")
##            if functions.check_change(lly1_old_array, lly1_new) == True:
##                print("\n------------------------------------------------------------------------------------\n" + "Prescience Point:")
##                print("LLY IPR")
##                lly1_old_array.append(lly1_new)
##                winsound.Beep(Freq, Dur)
##                webbrowser.open("https://ptab.uspto.gov/ptabe2e/rest/petitions/1461718/documents?availability=PUBLIC&cacheFix=")
##                time.sleep(30) #delay half second
##                if len(lly1_old_array) > 5:
##                    del lly1_old_array[0]

        elif url == lly2_url:
            try:
                soup = BeautifulSoup(request.content, "lxml").text
                lly2_new = soup[1000:2000]
            except IndexError:
                lly2_new = lly2_old_array[-1]
                print("LLY IPR Error")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
                time.sleep(1)
                print("\n")
            except ConnectionError:
                print("LLY IPR connection error")
            if functions.check_change(lly2_old_array, lly2_new) == True:
                print("\n------------------------------------------------------------------------------------\n")
                print("LLY IPR")
                lly2_old_array.append(lly2_new)
                winsound.Beep(Freq, Dur)
                webbrowser.open("https://ptab.uspto.gov/ptabe2e/rest/petitions/1463994/documents?availability=PUBLIC&cacheFix=")
                time.sleep(30) #delay half second
                if len(lly2_old_array) > 5:
                    del lly2_old_array[0]
            time.sleep(.5)

threads=[]
for item in urls:
    t=threading.Thread(target=getSite, args=(item,))
    threads.append(t)
    t.start()
click = threading.Thread(target=mouse_click.refresh_cnbc(1500))
click.start()




