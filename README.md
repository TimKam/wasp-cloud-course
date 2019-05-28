# Matrix Computation with Apache Spark in the Cloud

*Christopher Blöcker, Timotheus Kampik, Tobias Sundqvist*

This repository ([https://github.com/TimKam/wasp-cloud-course](https://github.com/TimKam/wasp-cloud-course)) contains documentation and example code for running matrix computations with Apache Spark in the cloud. 
The content was produced as part of the WASP Software Engineering and Cloud Computing Course 2019.

## Problem
The problem to solve is scaling *matrix computations* with Apache Spark. Instead of just running them on a local machine, the computations are to be executed across several cloud instances to speed up execution time. To demonstrate the performance advantage of the cloud-based solution, any of the matrices that are available at [https://sparse.tamu.edu/](https://sparse.tamu.edu/) and any of Spark's [linear algebra methods](https://spark.apache.org/docs/2.2.0/api/python/pyspark.ml.html#module-pyspark.ml.linalg) can be picked. However, the choice of data set and methods should allow for a fruitful analysis.

## Choice of Methods

Idea:

1. squared distance](https://spark.apache.org/docs/2.2.0/api/python/pyspark.ml.html#pyspark.ml.linalg.DenseVector.squared_distance) between all vectors in matrix

2. [dot product](https://spark.apache.org/docs/2.2.0/api/python/pyspark.ml.html#pyspark.ml.linalg.DenseVector.dot) between all vectors in matrix

## Choice of Data Set

Idea: just to pick something that "feels" medium size among the data sets after sorting them by number non-zero entries: https://sparse.tamu.edu/LPnetlib/lpi_ceria3d

## Setup
The Docker/Spark setup is taken from [this blog post by Marco Villarreal](https://medium.com/@marcovillarreal_40011/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-ba9d743a157f).


## Execution

## Analysis