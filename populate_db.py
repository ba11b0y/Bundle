import sys
import django
import os
import csv
from main.models import GS
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bundle.settings")
django.setup()
rows = []
from main.models import *
from django.db.utils import IntegrityError
def conv_Date(a):
    a=a.split('-')
    mon = {
        'Jan':1,
        'Feb':2,
        'Mar':3,
        'Apr':4,
        'May':5,
        'Jun':6,
        'Jul':7,
        'Aug':8,
        'Sep':9,
        'Oct':10,
        'Nov':11,
        'Dec':12
    }
    a=a[2]+'-'+str(mon[a[1]])+'-'+a[0]
    return a

with open('1.csv') as f:
     csv_reader = csv.reader(f, delimiter=',')
     for row in csv_reader:
            rows.append(row)

try:
    for x in range(3, len(rows)):
        gs = GS(isin=rows[x][0], return_rate=float(rows[x][1].split('%')[0]), date_of_issue=conv_Date(rows[x][2]),date_of_maturity=conv_Date(rows[x][3]),outstanding_stock= rows[x][4] )
        gs.save()
    print("seeded")
except IntegrityError:
    print(" already exists ")