import os
import csv

actual_folder = os.path.dirname(__file__)
csv_file_path = os.path.join(actual_folder, 'demo_file.csv')

data = []
with open(csv_file_path, 'r', encoding='utf8') as flux:
    curseur = (csv.reader(flux, delimiter=','))
    for e in curseur:
        data.append(e)

print(data)

new_csv_file_path = os.path.join(actual_folder, 'copie.csv')

with open(new_csv_file_path, 'w', encoding='utf8') as flux:
    curseur = csv.writer(flux, delimiter=';', lineterminator='\n')

    for line in data:
        curseur.writerow(line)

deces_csv_path = os.path.join(actual_folder, 'deces_usa.csv')

with open(deces_csv_path, 'r', encoding='utf8') as flux:
    curseur = csv.reader(flux)
    data = list(curseur)

for e in data[:5]:
    print(e)

header = data[:1]
data = data[1:]

years = [e[1] for e in data]
years_count = {}

for y in years:
    if y not in years_count:
        years_count[y] = 0

    years_count[y] += 1
print(years_count)

intends = [e[3] for e in data]
intends_count = {}

for i in intends:
    if i not in intends_count:
        intends_count[i] = 0
    intends_count[i] += 1

print(intends_count)



