import csv

with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader, None)

    for row in csv_reader:
        print(f'{row[0]} is {row[2]} and {row[1]} years old.')





