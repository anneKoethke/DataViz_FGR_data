# -*- coding: utf-8 -*-
import csv
import json

print('--- loading data ---')
currSaison = "16_17"
csv_file = open("csv_files/"+ currSaison +".csv", "r")
header = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST',
          'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']
csv_reader = csv.DictReader(csv_file, header)

allGames = []    # alle Spiele

print('--- processing data ---')
for row in csv_reader:
    gameDic = {'team': row['HomeTeam'], 'fouls': int(row['HF']), 'red': int(row['HR']), 'yellow': int(row['HY'])}
    allGames.append(gameDic)
    gameDic = {'team': row['AwayTeam'], 'fouls': int(row['AF']), 'red': int(row['AR']), 'yellow': int(row['AY'])}
    allGames.append(gameDic)

teamList = []   # alle Vereine
for game in allGames:
    if not game['team'] in teamList:
        teamList.append(game['team'])

saison = []
for team in teamList:
    teamDic = {'team': team, 'fouls': 0, 'red': 0, 'yellow': 0}
    for game in allGames:
        if team == game['team']:
            teamDic['fouls'] += game['fouls']
            teamDic['red'] += game['red']
            teamDic['yellow'] += game['yellow']
    saison.append(teamDic)


bundesliga = {
    'saison_'+currSaison: saison
}

print(bundesliga) # läuft!

print("--- writing to file ---")

# Ausgabe als JSON
with open('saison_'+currSaison+'.json', 'w', encoding='utf-8') as json_file:
    json.dump(bundesliga, json_file, indent=2)

print("--- finished ---")
