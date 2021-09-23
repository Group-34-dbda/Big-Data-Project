#! /bin/python

import pyspark
from pyspark.sql import SparkSession
from pyspark import SparkContext
#import sys

#print(sys.argv)

sc = SparkContext("local", "DemoContext")
sc.setLogLevel ("FATAL")

#hdfsLink = 'hdfs://ec2-3-91-63-206.compute-1.amazonaws.com'
#hdfsLink = sys.argv[1]

ss = SparkSession.builder.master("local").appName("DemoSession").getOrCreate()

print("Creating Dataframes\n")
backersDF = ss.read.option("header",True).csv('s3://projecdataset/data2/backers.csv')
candidatesDF = ss.read.option("header",True).csv('s3://projecdataset/data2/candidates.csv')
individual_contributionsDF = ss.read.option("header",True).csv('s3://projecdataset/data2/individual_contributions.csv')
politiciansDF = ss.read.option("header",True).csv('s3://projecdataset/data2/politicians.csv')
fec_api_committeesDF = ss.read.option("header",True).csv('s3://projecdataset/data2/fec_api_committees.csv')
pacsDF = ss.read.option("header",True).csv('s3://projecdataset/data2/pacs.csv')
committeesDF = ss.read.option("header",True).csv('s3://projecdataset/data2/committees.csv')
pac_recordsDF = ss.read.option("header",True).csv('s3://projecdataset/data2/pac_records.csv')
pac_to_pacsDF = ss.read.option("header",True).csv('s3://projecdataset/data2/pac_to_pacs.csv')




print("Individual Contibutions Summary")
individual_contributionsDF.describe(["amount"]).show()

print("Show Data")
backersDF.show()
candidatesDF.show()
politiciansDF.show()
fec_api_committeesDF.show()
pacsDF.show()
committeesDF.show()
pac_recordsDF.show()
pac_to_pacsDF.show()



