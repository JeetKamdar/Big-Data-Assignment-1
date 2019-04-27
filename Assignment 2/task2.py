#!/usr/bin/env python

import sys
from pyspark import SparkContext
from csv import reader

sc = SparkContext()
lines = sc.textFile(sys.argv[1])
lines = lines.mapPartitions(lambda x: reader(x))

parking_violations_count = lines.map(lambda x: (x[2], 1)).reduceByKey(lambda x, y: x + y)
formatted_count = parking_violations_count.map(lambda x: ("%s\t%d" % (x[0], x[1])))
formatted_count.saveAsTextFile("task2.out")
