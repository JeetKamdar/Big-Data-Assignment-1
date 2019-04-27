#!/usr/bin/env python

import sys
from pyspark.sql import SparkSession
from csv import reader

from pyspark.sql.functions import format_string

spark = SparkSession.builder.appName("task2SQL").getOrCreate()
parking_violation = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])
parking_violation.createOrReplaceTempView("parking")

result = spark.sql("SELECT violation_code, count(violation_code) violation_count FROM parking GROUP BY violation_code")

result.select(format_string('%s\t%d',result.violation_code,result.violation_count)).write.save("task2-sql.out",format="text")