import json

saison_keys = ['saison_06_07', 'saison_07_08', 'saison_08_09', 'saison_09_10', 'saison_10_11', 'saison_11_12', 'saison_12_13', 'saison_13_14', 'saison_14_15', 'saison_15_16', 'saison_16_17']

i = 0
j = 0
total = []
total_teamList = []
saisons = []

with open("copy.json", "r") as read_file:
    data = json.load(read_file)
    for d in data:
        # print(saison.keys()) erzeugt die saison_keys (oben)
        # print(saison[saison_keys[i]])
        for entry in d[saison_keys[i]]:
            saisons.append(entry)
            if not entry['team'] in total_teamList:
                total_teamList.append(entry['team'])
        i += 1

    for team in total_teamList:
        teamDic = {'team': team, 'fouls': 0, 'red': 0, 'yellow': 0}
        for game in saisons:
            # print(game)
            if team == game['team']:
                teamDic['fouls'] += game['fouls']
                teamDic['red'] += game['red']
                teamDic['yellow'] += game['yellow']
        total.append(teamDic)
# print(total_teamList)
# print(len(total_teamList))
# print(saisons)
# print(len(total))
# print(total)

'''with open("FGR_total.json", "w", encoding="utf-8") as json_file:
    json.dump(total, json_file, indent=2)

print("finished")'''