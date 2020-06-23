import csv


def get_csv_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the csv file
    data_file = open(file_name, 'r')
    # create a csv reader from csv file
    reader = csv.reader(data_file)
    # skip the headers
    next(reader)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows