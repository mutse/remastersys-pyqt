#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright (C) 2013 mutse
#
# Author: mutse <yyhoo2.young@gmail.com>
#

import subprocess

def output(cmd1, cmd2):
	p1 = subprocess.Popen(cmd1, shell = True, stdout = subprocess.PIPE)
	p2 = subprocess.Popen(cmd2, shell = True, stdin = p1.stdout, stdout = subprocess.PIPE)
	p1.stdout.close()
	return p2.communicate()[0].strip('\n')

def list_user():
	p = subprocess.Popen("cat /etc/passwd", shell = True, stdout = subprocess.PIPE)

	for line in p.stdout.readlines():
		line = line.strip('\n')
		cmd = "echo \"%s\"" % (line)
		userId = output(cmd, "cut -d \":\" -f3")
		cmd = "echo %s" % (userId)
		s = output(cmd, "grep \'^[[:digit:]]*$\'")
		if s:
			ID = int(userId)
			if ID > 999 and ID < 2000:
				cmd = "echo %s" % (line)
				name = output(cmd, "cut -d \":\" -f1")
				print "%s" % (name)
		else:
			continue

if __name__ == "__main__":
	list_user()

