#getMatchDetail
# get match details

# Kick-off time, Half-time, Full-time, Goals, Lineups, substitutes, referee
# general game stats


import urllib2
import json
from bs4 import BeautifulSoup
import pandas as pd
import time #for sleep function

l = "http://int.soccerway.com/matches/2014/11/02/hong-kong/hkfa-1st-division/wong-tai-sin-district-recreation--sports-council/yuen-long/1924697/?ICID=PL_MS_02"

#response = urllib2.urlopen(l)
#html = response.read()


#text_file = open("Output.txt", "wb")
#text_file.write(html)
#text_file.close()

text_file = open("Output.txt", "rb")
html = text_file.read()
text_file.close()

soup = BeautifulSoup(html)
kickoffTime = soup.find_all('span', attrs={"class":"timestamp","data-format":"HH:MM"})[0].contents[0]

t = soup.find_all("div", attrs={"class":"details clearfix"})
halfTimeScore = t[1].find_all("dd")[0].contents[0]
fullTimeScore = t[1].find_all("dd")[1].contents[0]

t = soup.find_all("table", attrs={"class":"matches events"})

goalMinutes = []
for minute in t[0].find_all("span", attrs={"class":"minute"}):
	goalMinutes.append(minute.contents[0])

print goalMinutes

goals = []
for g in t[0].find_all("td", attrs={"class":"event-icon"}):
	goals.append(g.div.contents[0])

scorers = []
scorerLinks = []
for s in t[0].find_all("a"):
	scorerLinks.append(s['href'])
	scorers.append(s.contents[0])

#referee
referee = []
refereeLink = []
t = soup.find_all("a", attrs={"class":"flag_16 left_16 hong-kong_16_left referee"})
referee = t[0].contents
refereeLink = t[0]['href']


