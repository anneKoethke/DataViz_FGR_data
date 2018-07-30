import csv
import json
files = ["csv_files/06_07.csv", "csv_files/07_08.csv", "csv_files/08_09.csv", "csv_files/09_10.csv", "csv_files/10_11.csv", "csv_files/11_12.csv", "csv_files/12_13.csv", "csv_files/13_14.csv", "csv_files/14_15.csv", "csv_files/15_16.csv", "csv_files/16_17.csv"]

arr = []
for file in files:
    csv_file = open(file, "r")
    header = ['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HTHG', 'HTAG', 'HTR', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF', 'HC', 'AC', 'HY', 'AY', 'HR', 'AR']
    csv_reader = csv.DictReader(csv_file, header)

    for row in csv_file:
        dic = {}
        print(type(row))
        dic['Date'] = row['Date']
        dic['HomeTeam'] = row['HomeTeam']
        dic['AwayTeam'] = row['AwayTeam']
        dic['HF'] = row['HF']
        dic['AF'] = row['AF']
        dic['HY'] = row['HY']
        dic['AY'] = row['AY']
        dic['HR'] = row['HR']
        dic['AR'] = row['AR']
        arr.append(dic)

FGR = {
    "allGames" : arr
}

print(FGR)