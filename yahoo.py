#!/usr/bin/env python

from time import ctime
from urllib import urlopen

ticks=('YAOO', 'GOOG', 'EBAY', 'AMAZ')
URL='http://quote.yahoo.com/d/quotes.csv?s=%s&f=sllclp2'

print '\nPrinces quoted as of:',ctime()
print '\nTICKER'.ljust(8),'PRICE'.ljust(8),'CHG'.ljust(5),'AGE'
print '------'.ljust(8),'------'.ljust(8),'------'.ljust(5),'------'
u=urlopen(URL % ','.join(ticks))

for row in u:
	tick,price,chg,per = row.split(',')
	print eval(tick).ljust(7), \
		('%.2f' % round(float(price),2)).rjust(6), \
		chg.rjust(6),eval(per.rstrip()).rjust(6)