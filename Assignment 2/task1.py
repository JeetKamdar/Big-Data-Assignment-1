#!/usr/bin/env python

import sys
from pyspark import SparkContext
from csv import reader

def my_counter(x, y):
	return (0, 0)

def format_output(x):
		return ("%s\t%s, %s, %s, %s" % (x[0], x[1][3], x[1][4],x[1][2],x[1][1]))

sc = SparkContext()

parking_violations_lines = sc.textFile(sys.argv[1])
parking_violations_lines = parking_violations_lines.mapPartitions(lambda x: reader(x))
parking_violations = parking_violations_lines.map(lambda x: (x[0], (1, x[1], x[2], x[-8], x[-16])))

open_violations_lines = sc.textFile(sys.argv[2])
open_violations_lines = open_violations_lines.mapPartitions(lambda x: reader(x))
open_violations = open_violations_lines.map(lambda x: (x[0], (0, 'O')))

all_violations =  parking_violations.union(open_violations) \
									.reduceByKey(my_counter) \
									.filter(lambda x: x[1][0] == 1) \
									.sortByKey() \
									.map(format_output) \
									.saveAsTextFile("task1.out")
