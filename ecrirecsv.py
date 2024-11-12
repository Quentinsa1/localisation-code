import csv
with open('data.csv', mode ='r') as file:
    csv_reader = csv.DictReader(file)
    for line in csv_reader: 
        print(line)