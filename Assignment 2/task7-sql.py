#!/usr/bin/env python

import sys
from pyspark.sql import SparkSession
from csv import reader

from pyspark.sql.functions import format_string

spark = SparkSession.builder.appName("task2SQL").getOrCreate()
parking_violation = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])
parking_violation.createOrReplaceTempView("parking")


violation = spark.sql("SELECT violation_code, date_format(issue_date,'dd-MM-yyyy') date_issued FROM parking") 
violation.createOrReplaceTempView("violation")
violation_transform = spark.sql("SELECT violation_code, CASE WHEN date_issued like '05-%' or date_issued like '06-%' or date_issued like '12-%' or date_issued like '13-%' or date_issued like '19-%' or date_issued like '20-%' or date_issued like '26-%' or date_issued like '27-%' THEN 1.0 ELSE 0.0 END AS weekend FROM violation")
violation_transform.createOrReplaceTempView("violation_transform")
result = spark.sql("SELECT violation_code, sum(weekend) total_weekend, count(violation_code) total_violations FROM violation_transform GROUP BY violation_code")

#result.show()
result.select(format_string('%s\t%.2f, %.2f',result.violation_code, (result.total_weekend)/8.0, (result.total_violations - result.total_weekend)/23.0) ).write.save("task7-sql.out",format="text")
