#!/usr/bin/env python

import sys
from pyspark.sql import SparkSession
from csv import reader
from pyspark.sql.functions import date_format
from pyspark.sql.functions import format_string

spark = SparkSession.builder.appName("task2SQL").getOrCreate()

parking_violation = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])
open_violation = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[2])
parking_violation.createOrReplaceTempView("parking")
open_violation.createOrReplaceTempView("open")

closed_violations = spark.sql("SELECT p.summons_number, p.plate_id, p.violation_precinct, p.violation_code, p.issue_date FROM parking p WHERE p.summons_number in (SELECT p1.summons_number FROM parking p1 MINUS SELECT o.summons_number FROM open o)")
closed_violations.select(format_string('%d\t%s,%d, %d, %s',closed_violations.summons_number,closed_violations.plate_id,closed_violations.violation_precinct,closed_violations.violation_code,date_format(closed_violations.issue_date,'yyyy-MM-dd'))).write.save("task1-sql.out",format="text")
