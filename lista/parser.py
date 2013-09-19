# coding=utf-8
__author__ = 'jb'

import os, re

import tempfile
from stdnum import issn
import shutil
DIRNAME = os.path.split(__file__)[0]

DATA_FILE = "lista_c.pdf"

#ITEM_PATTERN = re.compile("\s*^\s*(\d+)\s*$\s*^\s*(\w*[\s\w]*\w+)+\s*$\s*^\s*(\d{4}-[\d]{3}[\dX])\s*$\s*^\s*(\d{2})\s*$\s*", re.MULTILINE)
#ITEM_PATTERN  = re.compile("\s*(\d+)\s*$\s*(\w*[\s\w]*\w+)\s*$\s*(\d{4}-[\d]{3}[\dX])\s*$\s*(\d{2})+\s*".replace("\w", "[a-zA-Z]"), re.MULTILINE)

ITEM_PATTERN  = re.compile("^\s*(\d+)\s+((?:[^\d]+)|(?:[^\-]+))\s+(\d{4}-[\d]{3}[\dX])\s+(\d{2})\s*$", re.MULTILINE | re.UNICODE)

def parse_file(data_file = DATA_FILE):

    import subprocess

    tmpdir = tempfile.mkdtemp()

    file = os.path.join(tmpdir, "data.txt")

    data_file = os.path.join(DIRNAME, "data", data_file)

    subprocess.check_call(["pdftotext",  "-raw", data_file, file])

    data = []

    with open(file) as f:
        DATA = f.read()

        groups = re.findall(ITEM_PATTERN, DATA)

    shutil.rmtree(tmpdir)

    return groups

def check_groups(groups):
    last_id = None
    errors = []
    for group in groups:
        this_id = int(group[0])
        if last_id is not None and not last_id == this_id -1:
            errors.append(u"Po czasopiśmie numer {} jest {}".format(last_id,  this_id))
            last_id = None
        else:
            last_id =  this_id
        if not issn.is_valid(group[2]):
            errors.append(u"Invalid issn '{}'".format(group[2]))

    return errors

if __name__ == "__main__":
    data = parse_file(DATA_FILE)
    print data
    check_groups(data)


