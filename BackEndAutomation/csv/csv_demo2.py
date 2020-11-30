import csv

with open('/Users/PycharmProjects/BackEndAutomation/utilities/loanapp.csv', 'a') as wfile:
    csv_writer = csv.writer(wfile)
    csv_writer.writerow(['Bob', 'Approved'])


with open('/Users/PycharmProjects/BackEndAutomation/utilities/loanapp.csv') as file:
    reader = csv.reader(file)
    print(list(reader))
