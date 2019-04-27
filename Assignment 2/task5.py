#!/usr/bin/env python

import sys
from pyspark import SparkContext
from csv import reader

sc = SparkContext()
lines = sc.textFile(sys.argv[1])
lines = lines.mapPartitions(lambda x: reader(x))

parking_violations_count = lines.map(lambda x: ((x[-8], x[-6]), 1)).reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1], False)
formatted_count = sc.parallelize(parking_violations_count.take(1)).map(lambda x: ("%s, %s\t%d" % (x[0][0], x[0][1], x[1])))
formatted_count.saveAsTextFile("task5.out")
