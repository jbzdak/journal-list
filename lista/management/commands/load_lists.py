__author__ = 'jb'

from optparse import make_option

from django.core.management.base import BaseCommand, CommandError, NoArgsCommand

from lista import parser
from lista import models



class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for file, cathegory in (("lista_a.pdf", 1), ("lista_b.pdf", 2), ("lista_c.pdf", 3)):
            erors = []
            print ("Importing: {}".format(file))

            groups = parser.parse_file(file)

            print(" There were following errors")
            print(parser.check_groups(groups))

            print ("Saving to db")

            ii = 0
            for item in groups:
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
                if ii % 100 == 0:
                    print "Done {} of {}".format(ii, len(groups))




