import csv

fileds = []
rows = []

with open("bmw_global_sales_2018_2025.csv") as f:
    dialect = csv.Sniffer().sniff(f.read(1024))
    print(dialect.delimiter)  # ,
    print(dialect.quotechar)  # "

    f.seek(0) # odczyt na początek
    csvreader = csv.reader(f)

    print(csvreader)

    fileds = next(csvreader)

    for row in csvreader:
        rows.append(row)

print('Fields:', fileds)
print('Rows:', rows[0])
