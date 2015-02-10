#getMatchResult 
# get simple match result (Date, score, teams) of each match 
# Source: http://int.soccerway.com/national/hong-kong/hkfa-1st-division/20142015/regular-season/r26927/matches/?ICID=PL_3N_02

# Use Chrome developer tool to copy the link when clicking the << Preivous OR Next >>


import urllib2
import json
from bs4 import BeautifulSoup
import pandas as pd
import time #for sleep function

dayOfWeek = []
date = []
homeTeam = []
awayTeam = []
homeScore = []
awayScore = []
matchDetailLink = []

links = ['http://int.soccerway.com/a/block_competition_matches?block_id=page_competition_1_block_competition_matches_6&callback_params={"page":"0","bookmaker_urls":[],"block_service_id":"competition_matches_block_competitionmatches","round_id":"26927","outgroup":"","view":"2"}&action=changePage&params={"page":-1}',
		'http://int.soccerway.com/a/block_competition_matches?block_id=page_competition_1_block_competition_matches_6&callback_params={"page":"-1","bookmaker_urls":[],"block_service_id":"competition_matches_block_competitionmatches","round_id":"26927","outgroup":"","view":"2"}&action=changePage&params={"page":0}',
		'http://int.soccerway.com/a/block_competition_matches?block_id=page_competition_1_block_competition_matches_6&callback_params={"page":"0","bookmaker_urls":[],"block_service_id":"competition_matches_block_competitionmatches","round_id":"26927","outgroup":"","view":"2"}&action=changePage&params={"page":1}']


#for each link, get the json content and parse
for l in links:	
	response = urllib2.urlopen(l)
	data = json.load(response)

	html = data['commands'][0]['parameters']['content']

	#text_file = open("Output.txt", "wb")
	#text_file.write(html)
	#text_file.close()

#text_file = open("Output.txt", "rb")
#html = text_file.read()
#text_file.close()

	soup = BeautifulSoup(html)

	#get the timestamp
	for s in soup.find_all('span'):
		#print s		
		if "ddd" in str(s):
			dayOfWeek.append(s.contents[0])
		elif "dd/mm/yy" in str(s):
			date.append(s.contents[0])

	#get home team of each match
	for s in soup.find_all('td', 'team-a'):
		homeTeam.append(s.contents[0].contents[0])

	#get away team of each match
	for s in soup.find_all('td', 'team-b'):
		awayTeam.append(s.contents[0].contents[0])


	#get score of each match
	for s in soup.find_all('td', 'score-time'):	
		href = s.contents[0].get('href')

		matchDetailLink.append(href)
		
		score = str(s.contents[0].contents[0])
		
		#split
		if score == "PSTP": #postpone
			h = "PSTP"
			a = "PSTP"
		elif ":" in score: # future match
			h = "TBD"
			a = "TBD"
		else:
			[h, a] = score.split("-")
		
		homeScore.append(h)
		awayScore.append(a)

	print "sleep for 1 second"
	time.sleep(1) #sleep for 1 second

#create dataframe and save to file
df = pd.DataFrame()
df['dayOfWeek'] = dayOfWeek
df['date'] = date
df['homeTeam'] = homeTeam
df['awayTeam'] = awayTeam
df['homeScore'] = homeScore
df['awayScore'] = awayScore
df['matchDetailLink'] = matchDetailLink

df.to_csv("matchResult.csv",encoding="utf-8", index=False)


