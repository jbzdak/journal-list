# coding=utf-8
from copy import copy
import csv
import subprocess

__author__ = 'jb'

import os

import tempfile
from stdnum import issn

import re

RE = re.compile("[\dX\-]+")

DIRNAME = os.path.split(__file__)[0]

DATA_FILE = "lista_c.pdf"

executable = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "extracttab.py")

def parse_page(args, last_no, page):

    fname = tempfile.mktemp()

    args.extend(['-p', str(page), '-o', fname])

    subprocess.check_call(args)

    warnings = []
    rows = []

    with open(fname) as f:
        r = csv.reader(f)
        for row in r:
            if  not row[0]:
                continue

            try:
                item_no = int(row[0])
                int(row[3])
            except ValueError:
                continue


            if not re.match(RE, row[2]) or not '-' in row[2]:
                continue

            if item_no != last_no + 1:
                warnings.append("Na stronie {} po czasopiśmie nr {} jest {}".format(page, last_no, item_no))



            rows.append(row)

            last_no = item_no

        return rows, warnings, last_no


def parse_file(last_page, data_file = DATA_FILE, first_page = 0):

    data_file = os.path.join(DIRNAME, 'data', data_file)

    args = [executable, '-i', os.path.abspath(data_file), '-t', 'table_csv']

    last_no = 1

    for page in range(first_page, last_page):
        result =  parse_page(copy(args), last_no, page)
        last_no = result[-1]
        yield result

def check_rows(groups):
    last_id = None
    errors = []
    for group in groups:
        if not issn.is_valid(group[2]):
            errors.append(u"Invalid issn '{}'".format(group[2]))

    return errors

if __name__ == "__main__":
    for rows, errors, __ in parse_file(49, DATA_FILE, 1):
        print(errors)
        print(check_rows(rows))


