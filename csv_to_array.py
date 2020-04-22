import csv

shortData = [['latitude', 'longitude', 'city', 'state', 'country', 'cases']]
visualizationData = [['latitude', 'longitude', 'cases']]

with open('04-20-2020.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count == 0): 
            line_count+=1
            continue
        try: 
            lat = float(row[3])
            lon = float(row[4])
            cases = float(row[5])
            visualizationData.append([lat,lon,cases])
        except ValueError: 
            continue

with open("updated_data.txt", "w") as f:
    for row in visualizationData:
        to_print = str(row)[1:-1]
        f.write("%s\n" % to_print)
    
f.close()