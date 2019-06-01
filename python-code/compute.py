# WASP cloud software course
# Tobias Sundqvist, Timotheus, Chris

#we use the findspark library to locate spark on our local machine
import findspark
from pyspark.mllib.linalg.distributed import  RowMatrix, IndexedRowMatrix,CoordinateMatrix, MatrixEntry
from pyspark.mllib.linalg import Matrices

#import matplotlib.pyplot as plt
#import seaborn as sns
from pyspark import SparkContext
sc = SparkContext()

#use local spark on computer
findspark.init('/home/sundqtob/spark_install/spark-2.1.0-bin-hadoop2.7')
from pyspark.sql import SparkSession
# initiate our session and read the main CSV file, then we print the #dataframe schema
spark = SparkSession.builder.appName('imbalanced_binary_classification').getOrCreate()
#new_df = spark.read.option("delimiter", " ").csv('data/1138_bus/1138_bus_no_head.mtx', header=False, inferSchema=True)
#new_df.printSchema()

rdd = sc.textFile('data/1138_bus/1138_bus_no_head.mtx')
rdd = rdd.map(lambda line: line.split(" "))
rdd = rdd.map(lambda line: [float(x) for x in line])

print(rdd.take(2))
#ncol = len(rdd.map(lambda r: r.image).first())
nrows = rdd.count()
ncols = 3
#matrix = Matrices.dense(nrows, ncols, rdd)
print("ncol: %d, nrow %d" %(ncols,nrows))
coord_mat = CoordinateMatrix(rdd.map(tuple))
print("num rows in matrix %d" %coord_mat.numRows())

print("finished using pyspark")
#________________________________________________-

print("now use SparkSession")


from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
df_2 = spark.read.option("delimiter", " ").csv('./data/lpi_ceria3d_b.mtx', header=False, inferSchema=True)
df_2.printSchema()

#coord_mat_2 = CoordinateMatrix(df_2.rdd.map(tuple))
row_mat = RowMatrix(df_2.rdd.map(tuple))
print("num rows in row matrix %d, num_cols %d" %(row_mat.numRows(),row_mat.numCols()))

print("print covariance")
print(row_mat.computeCovariance())

dm = Matrices.dense(3, 1, [4, 5, 6])

print("multiply row Matrix")
result = row_mat.multiply(dm)
