import csv

with open('/Users/PycharmProjects/BackEndAutomation/utilities/loanapp.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # print(csv_reader)
    # print(list(csv_reader))
    names = []
    statuses = []
    for row in csv_reader:
        # print(row)
        # print(row[0])
        names.append(row[0])
        statuses.append(row[1])

    print(names[1:])
    print(statuses[1:])

    name_index = names.index('Sam')
    print(f"Sam's status is {statuses[name_index]}")

    for n, s in zip(names, statuses):
        if n == 'Sam':
            print(s)
