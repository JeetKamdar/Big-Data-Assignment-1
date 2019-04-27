#!/usr/bin/env python

import sys
from pyspark.sql import SparkSession
from csv import reader

from pyspark.sql.functions import format_string

spark = SparkSession.builder.appName("task3SQL").getOrCreate()
open_violation = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])
open_violation.createOrReplaceTempView("open_violation")

result = spark.sql("SELECT license_type, sum(amount_due) total_due, avg(amount_due) avg_due FROM open_violation GROUP BY license_type ORDER BY license_type")

result.select(format_string('%s\t%.2f, %.2f',result.license_type,result.total_due, result.avg_due)).write.save("task3-sql.out",format="text")