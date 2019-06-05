# WASP cloud software course
# Tobias Sundqvist, Timotheus Kampik, Christopher Blöcker
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
#import urllib.request

#import findspark
import pyspark
from pyspark.mllib.linalg.distributed import CoordinateMatrix, MatrixEntry
#from pyspark.mllib.linalg.distributed import RowMatrix
from pyspark.mllib.linalg import Matrices

from pyspark import SparkConf, SparkContext, SparkFiles
from pyspark.sql import SparkSession

#parser = ArgumentParser()
#parser.add_argument('-u', "--url", dest="spark_url", help="URL of the Spark master")
#args = parser.parse_args()

spark = SparkSession\
        .builder\
        .appName("linalgtest")\
        .getOrCreate()

#conf = SparkConf().setAppName('linalgtest')
#sc = SparkContext(conf=conf).getOrCreate()

#use local spark on computer
# findspark.init()
#from pyspark.sql import SparkSession

local_file_location = 'file:///wasp/pdb1HYS.mtx.mtx'

rdd = spark.sparkContext.textFile(local_file_location)
rdd = rdd.map(lambda line: line.split(" "))
rdd = rdd.map(lambda line: MatrixEntry(int(line[0]), int(line[1]), float(line[2])))

mat = CoordinateMatrix(rdd)
M  = mat.toRowMatrix()
A  = mat.toBlockMatrix()
At = mat.transpose().toBlockMatrix()

print("SVD")
print(M.numRows(), M.numCols())
start_svd = time.time()

NUM_TIMES=10
#do it 10 times to get mean
for i in range(NUM_TIMES):
    svd = M.computeSVD(5, computeU=True)

end_svd = time.time()
print("Time elapsed: ", (end_svd - start_svd)/NUM_TIMES) # CPU seconds elapsed (floating point)

print("multiply Matrix")
start_mul = time.time()

for i in range(NUM_TIMES):
    AAt = A.multiply(At)

end_mul = time.time()
print("Time elapsed: ", (end_mul - start_mul)/NUM_TIMES) # CPU seconds elapsed (floating point)

print("finished using pyspark")

print("SVD: ", (end_svd - start_svd)/NUM_TIMES) # CPU seconds elapsed (floating point)
print("Mul: ", (end_mul - start_mul)/NUM_TIMES) # CPU seconds elapsed (floating point)

spark.stop()