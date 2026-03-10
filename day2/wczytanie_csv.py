import csv

with open("bmw_global_sales_2018_2025.csv") as f:
    csvreader = csv.reader(f)

    print(csvreader)