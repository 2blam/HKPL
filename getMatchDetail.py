#getMatchDetail
# get match details

# Kick-off time, Half-time, Full-time, Goals, Lineups, substitutes, referee
# Note: 
#	Some games do not provide the general game stats
#   Need to check if hkfa would provide this data
#


import urllib2
import json
from bs4 import BeautifulSoup
import pandas as pd
import time #for sleep function
import re 

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

#get match ID
matchID = soup.find_all('li', attrs={"class":"current"})[0].contents[0]['href']
matchID = re.findall('/\d+/', matchID)[-1][1:-1] #get the last occurrence

# basic info
kickoffTime = soup.find_all('span', attrs={"class":"timestamp","data-format":"HH:MM"})[0].contents[0]
t = soup.find_all("div", attrs={"class":"details clearfix"})
halfTimeScore = t[1].find_all("dd")[0].contents[0]
fullTimeScore = t[1].find_all("dd")[1].contents[0]

t = soup.find_all("table", attrs={"class":"matches events"})

#goals details
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

#lineups
t = soup.find_all("table", attrs={"class":"playerstats lineups table"})
#home team
homeLineups = []
for p in t[0].find_all('a')[0:11]:
	homeLineups.append(p['href'])	

homeCoach = t[0].find_all('a')[11]['href']

#away team 
awayLineups = []
for p in t[1].find_all('a')[0:11]:
	awayLineups.append(p['href'])	

awayCoach = t[1].find_all('a')[11]['href']

#substitutes
t = soup.find_all("table", attrs={"class":"playerstats lineups substitutions table"})
#home team
homeSubstitutes = []
for s in t[0].find_all('a'):
	homeSubstitutes.append(s['href'])	

#remove the subtitutes-in
homeSub = set(homeSubstitutes) - set(homeLineups)
#homeSubIn = set(homeSubstitutes).intersection(set(homeLineups))

awaySubstitutes = []
for s in t[1].find_all('a'):
	awaySubstitutes.append(s['href'])	

#remove the subtitutes-in
awaySub = set(awaySubstitutes) - set(awayLineups)
#homeSubIn = set(homeSubstitutes).intersection(set(homeLineups))



#away team
awaySubstitutes = []
for s in t[1].find_all('a'):
	awaySubstitutes.append(s['href'])	


#referee
referee = []
refereeLink = []
t = soup.find_all("a", attrs={"class":"flag_16 left_16 hong-kong_16_left referee"})
referee = t[0].contents
refereeLink = t[0]['href']




#get general game stats chart
#statsLink = "http://int.soccerway.com/charts/statsplus/1924697/"
#response = urllib2.urlopen(statsLink)
#html = response.read()

#text_file = open("stats.txt", "wb")
#text_file.write(html)
#text_file.close()

text_file = open("stats.txt", "rb")
html = text_file.read()
text_file.close()





