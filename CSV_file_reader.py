import csv

with open("data.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            next(csv_file)
            line_count = 1
        else:
            print(f'{row[0]} is {row[2]} and {row[1]} years old.')
            line_count += 1




