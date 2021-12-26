import csv

dataset1 = []
dataset2 = []

with open("data1.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        dataset1.append(row)

with open("data2_sorted.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        dataset2.append(row)

headers1 = dataset1[0]
planet_data1 = dataset1[1:]

headers2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = headers1+headers2
planet_data = []
for index, datarow in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("final.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)