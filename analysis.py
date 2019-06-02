# WASP cloud software course
# Tobias Sundqvist, Timotheus, Chris
# 
# prerequisite:
# - java 8 jre:
# sudo apt install openjdk-8-jre-headless
# -install spark:
# mkdir spark_install && cd spark_install
# wget http://d3kbcqa49mib13.cloudfront.net/spark-2.1.0-bin-hadoop2.7.tgz
# tar -xzvf spark-2.1.0-bin-hadoop2.7.tgz 

# - pip install numpy
# - pip install findspark
# - pip install pyspark

# download data: 
# Si87H76 : https://sparse.tamu.edu/MM/PARSEC/Si87H76.tar.gz
# remove the comments in the beginning of the datafile (14 lines) use following command to remove the 14 first lines: (sed -i 1,14d Si87H76.mtx)
#
# time to run on virtual box env:
# pca: 260.14 sec   and 275.56 sec                                       
# multiply row Matrix 0.0194 sec and 0.0295 sec

from argparse import ArgumentParser
import time
import urllib.request

import findspark
import pyspark
from pyspark.mllib.linalg.distributed import  RowMatrix
from pyspark.mllib.linalg import Matrices

from pyspark import SparkConf, SparkContext, SparkFiles

parser = ArgumentParser()
parser.add_argument('-u', "--url", dest="spark_url", help="URL of the Spark master")
args = parser.parse_args()

conf = SparkConf().setAppName('linalgtest').setMaster(args.spark_url)
sc = SparkContext(conf=conf)

#use local spark on computer
# findspark.init()
#from pyspark.sql import SparkSession

local_file_location = 'file:///usr/local/data/Si87H76_no_head.mtx'

rdd = sc.textFile(local_file_location)
rdd = rdd.map(lambda line: line.split(" "))
rdd = rdd.map(lambda line: [float(x) for x in line])

row_mat = RowMatrix(rdd.map(tuple))

print("print principalComponents")
start = time.time()

NUM_TIMES=10
#do it 10 times to get mean
for i in range(0, NUM_TIMES):
    result_principal = row_mat.computePrincipalComponents(2)

end = time.time()
print("Time elapsed: ", (end - start)/NUM_TIMES) # CPU seconds elapsed (floating point)

print(result_principal)

dm = Matrices.dense(3, 1, [4, 5, 6])

print("multiply row Matrix")
start = time.time()

for i in range(0, NUM_TIMES):
    result = row_mat.multiply(dm)

end = time.time()
print("Time elapsed: ", (end - start)/NUM_TIMES) # CPU seconds elapsed (floating point)

print("finished using pyspark")
