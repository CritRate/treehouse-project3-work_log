import csv
from datetime import datetime
import re

from clear_console import clear
from print_entries import print_entries


def date_search():
    entries = []
    while True:
        try:
            print('Enter the date')
            date = input('Please use DD/MM/YYYY: ')
            valid_date = datetime.strptime(date, '%d/%m/%Y')
            break
        except:
            print(f'{date} is not a valid date')
            input('Press enter to try again')
            clear()
            continue
    with open('log.csv', 'r', newline='') as csvfile:
        fieldnames = ['date', 'title', 'time', 'notes']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for line_number, entry in enumerate(reader):
            if line_number == 0:
                continue
            if valid_date == datetime.strptime(entry['date'], '%Y-%m-%d'):
                entries.append((line_number, entry))
        print_entries(entries)


def date_range_search():
    entries = []
    while True:
        try:
            print('Enter the date range')
            date1 = input('Please use DD/MM/YYYY date #1: ')
            date2 = input('Please use DD/MM/YYYY date #2: ')
            valid_date1 = datetime.strptime(date1, '%d/%m/%Y')
            valid_date2 = datetime.strptime(date2, '%d/%m/%Y')
            break
        except:
            print('One of the date are not a valid date')
            input('Press enter to try again')
            clear()
            continue
    with open('log.csv', 'r', newline='') as csvfile:
        fieldnames = ['date', 'title', 'time', 'notes']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for line_number, entry in enumerate(reader):
            if line_number == 0:
                continue
            date = datetime.strptime(entry['date'], '%Y-%m-%d')
            # does not matter which value is higher
            if valid_date1 < valid_date2:
                if valid_date1 <= date <= valid_date2:
                    entries.append((line_number, entry))
            else:
                if valid_date1 >= date >= valid_date2:
                    entries.append((line_number, entry))
        print_entries(entries)


def regex_search():
    entries = []
    pattern = input()
    raw_pattern = r'{}'.format(pattern)
    compiled_pattern = re.compile(raw_pattern, re.I)
    with open('log.csv', 'r', newline='') as csvfile:
        fieldnames = ['date', 'title', 'time', 'notes']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for line_number, entry in enumerate(reader):
            if line_number == 0:
                continue
            if (compiled_pattern.search(entry['title']) or
                    compiled_pattern.search(entry['notes'])):
                entries.append((line_number, entry))
        print_entries(entries)
