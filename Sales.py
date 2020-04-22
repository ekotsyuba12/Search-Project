import csv


a_sale = []

with open ('Copy of sales.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader (csv_file)

    for row in spreadsheet:
        a_sale.append (int(row ['sales']))

    total = sum(a_sale)
    average = round(int(total)/12, 2)
    high = max(a_sale)
    low = min (a_sale)
    print ('Annual sales: {}'.format(total))
    print('Average number of sales during the year: {}'.format(average))
    print ('Highest Sale: {}'.format(high), 'Lowest sale: {}'.format(low))
