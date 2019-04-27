#!/usr/bin/env python

import sys
from pyspark.sql import SparkSession
from csv import reader

from pyspark.sql.functions import format_string

spark = SparkSession.builder.appName("task2SQL").getOrCreate()
parking_violation = spark.read.format('csv').options(header='true',inferschema='true').load(sys.argv[1])
parking_violation.createOrReplaceTempView("parking")

state_transform = spark.sql("SELECT CASE WHEN registration_state like '%NY%' THEN 'NY' ELSE 'Other' END AS state FROM parking")
state_transform.createOrReplaceTempView("state_transform")
my_count = spark.sql("SELECT state, count(state) registration_state_count FROM state_transform GROUP BY state")

my_count.select(format_string('%s\t%d',my_count.state ,my_count.registration_state_count)).write.save("task4-sql.out",format="text")
