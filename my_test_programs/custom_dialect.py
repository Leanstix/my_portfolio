#!/usr/bin/python3

import csv

# Define a custom dialect
class MyDialect(csv.Dialect):
    delimiter = ';'
    quotechar = '"'
    escapechar = '\\'
    doublequote = True
    skipinitialspace = True
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL

# Register the custom dialect
csv.register_dialect('my_dialect', MyDialect)

if __name__ == "__main__":
    # Example of writing a CSV file using the custom dialect
    with open('custom_dialect.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='my_dialect')
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerow(['Alice', '30', 'New York'])
        writer.writerow(['Bob', '25', 'Los Angeles'])
        writer.writerow(['Charlie', '35', 'Chicago'])

    # Example of reading a CSV file using the custom dialect
    with open('custom_dialect.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, dialect='my_dialect')
        for row in reader:
            print(row)
