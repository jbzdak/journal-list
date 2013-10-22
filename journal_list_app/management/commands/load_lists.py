import os

__author__ = 'jb'



from optparse import make_option

from django.core.management.base import BaseCommand, CommandError, NoArgsCommand

import journal_list_app

from journal_list_app import parser
from journal_list_app import models


CATH = (
    ("lista_a.pdf", 1, 1, 261),
    ("lista_b.pdf", 2, 1, 49),
    ("lista_c.pdf", 3, 1, 113)
)



class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for file, cathegory, first_page, last_page in CATH:
            erors = []
            print ("Importing: {}".format(file))


            print(" There were following errors")


            print ("Saving to db")

            ii = 0

            for rows, errors, __ in parser.parse_file(last_page, file, first_page):

                if errors:
                    print(errors)

                errors = parser.check_rows(rows)

                if errors:
                    print(errors)

                for item in rows:
                    journal, created = models.Journal.objects.get_or_create(
                        issn = item[2],
                        defaults = {
                            'name' : item[1],
                            'pts' : item[3],
                            'cathegory' : cathegory
                        }

                    )

                    if not created:
                        journal.name = item[1],
                        journal.pts = item[3]
                        journal.cathegory = cathegory
                        journal.save()
                    ii+=1




