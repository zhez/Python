#!/usr/bin/env python

import ftplib
import os
import socket

HOST='venturev.w40-e0.ezcname.com'
DIRN='wwwroot'
FILE='index.html'

def main():
	try:
		f=ftplib.FTP(HOST)
	except(socket.error,socket.gaierror),e:
		print 'ERROR: cannot reach "%s"' % HOST
		return
	print '*** Connected to host "%s"' % HOST

	try:
		f.login()
	except ftplib.error_perm:
		print 'ERROR: cannot login anonymously'
		f.quit
		return
	print '*** Logged in as "anonymous"'

	try:
		f.cwd(DIRN)
	except fptlib.error_perm:
		print 'ERROR: cannot CD to "%s"' % DIRN
		f.quit
		return
	print '*** Changd to "%s" folder' % FILE

	try:
		f.retrbinary('RETR %s' %FILE,open(FILE,'wb').write)
	except ftplib.error_perm:
		print 'ERROR: cannot read file "%s"' %FILE
		os.unlink(FILE)
	else:
		print '*** Downloaded "%s" to CWD' % FILE
	f.quit()
	return

if __name__=='__main__':
	main()