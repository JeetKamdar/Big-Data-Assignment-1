#!/usr/bin/env python

import sys
from pyspark import SparkContext
from csv import reader

def format_output(lines):
		return ("%s\t%.2f, %.2f" % (lines[0], lines[1][0]/int(lines[1][1]), lines[1][2]/int(lines[1][3])) )

def my_mapper(x):
	if int(x[1][8:10]) %7 == 5 or int(x[1][8:10]) %7 == 6:
		return (x[2], (1, '8', 0, '23'))
	else:
		return (x[2], (0, '8', 1, '23'))

sc = SparkContext()
lines = sc.textFile(sys.argv[1])
lines = lines.mapPartitions(lambda x: reader(x))
parking_violations_count = lines.map(my_mapper) \
								.reduceByKey(lambda x, y: (x[0]+y[0], x[1], x[2]+y[2], x[3]) ) \
								.sortByKey() \
								.map(format_output) \
								.saveAsTextFile("task7.out")
