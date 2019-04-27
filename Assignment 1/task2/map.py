#!/usr/bin/env python

import sys
import string

for line in sys.stdin:
	line = line.strip()
	entry = line.split(",")
	print("%s\t1" % entry[2])