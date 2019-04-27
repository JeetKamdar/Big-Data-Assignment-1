#!/usr/bin/env python

import sys
from pyspark import SparkContext
from csv import reader

sc = SparkContext()
lines = sc.textFile(sys.argv[1])
lines = lines.mapPartitions(lambda x: reader(x))

violation_type = lines.map(lambda x: (x[2], (float(x[-6]), 1.00)))
total_amount_due = violation_type.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))
formatted_count = total_amount_due.map(lambda x: ("%s\t%.2f, %.2f" % (x[0], x[1][0], x[1][0]/x[1][1])))
formatted_count.saveAsTextFile("task3.out")
