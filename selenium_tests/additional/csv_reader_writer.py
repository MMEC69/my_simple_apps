import csv

with open('../datasets/sample1.csv', mode='r', encoding='utf-8') as file:
    # Create a reader object
    csv_reader = csv.reader(file)

    # Optional: Skip the header row if your file has one
    header = next(csv_reader)

    # Iterate through the rows
    for row in csv_reader:
        print(row)  # Each row is a list, e.g., ['John', '30', 'New York']
