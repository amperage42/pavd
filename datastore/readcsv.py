#!/usr/bin/python3

import csv

class CSVDetails():
    def __init__(self, filename):
        with open(filename, "r") as f_input:
            csv_input = csv.reader(f_input)
            self.details = list(csv_input)

    def get_col_row(self, col, row):
        return self.details[row-1][col-1]

    def set_col_row(self, col, row, data):
        self.details[row-1][col-1] = data
