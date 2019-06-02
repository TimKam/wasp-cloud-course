# Matrix Computation with Apache Spark in the Cloud

*Christopher Blöcker, Timotheus Kampik, Tobias Sundqvist*

This repository ([https://github.com/TimKam/wasp-cloud-course](https://github.com/TimKam/wasp-cloud-course)) contains documentation and example code for running matrix computations with Apache Spark in the cloud.
The content was produced as part of the WASP Software Engineering and Cloud Computing Course 2019.

## Problem
The problem to solve is scaling *matrix computations* with Apache Spark. Instead of just running them on a local machine, the computations are to be executed across several cloud instances to speed up execution time. To demonstrate the performance advantage of the cloud-based solution, any of the matrices that are available at [https://sparse.tamu.edu/](https://sparse.tamu.edu/) and any of Spark's [linear algebra methods](https://spark.apache.org/docs/2.2.0/api/python/pyspark.ml.html#module-pyspark.ml.linalg) can be picked. However, the choice of data set and methods should allow for a fruitful analysis.

## Choice of Methods
To assess the performance of an Apache Spark cluster with different numbers of worker nodes for a linear algebra use case, we chose the following methods:

1. **Principal component analysis** (PCA): [pyspark.mllib.linalg.distributed.RowMatrix.computePrincipalComponents](https://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#pyspark.mllib.linalg.distributed.RowMatrix.computePrincipalComponents);

2. **Multiply**: [pyspark.mllib.linalg.distributed.RowMatrix.multiply](https://spark.apache.org/docs/latest/api/python/pyspark.mllib.html#pyspark.mllib.linalg.distributed.RowMatrix.multiply)

We picked the two methods, because we expect them to be commonly used in real-life scenarios.

## Choice of Data Set

Idea: just to pick something that "feels" medium size among the data sets after sorting them by number non-zero entries: https://sparse.tamu.edu/LPnetlib/lpi_ceria3d

## Setup
The Docker/Spark setup is taken from [this blog post by Marco Villarreal](https://medium.com/@marcovillarreal_40011/creating-a-spark-standalone-cluster-with-docker-and-docker-compose-ba9d743a157f).


## Execution
Build the images with `make`. Then spin up the cluster with `docker-compose up -d`. Spin up a submit container to run something in the cluster with something like

```
docker run -ti --rm --network=$NETWORK -v <script path>:/scripts spark-submit:2.3.1 /bin/bash
```

where `NETWORK` is the Docker network to which the containers are connected and `<script path>` is where the *executables* are. Find out the network with `docker network ls`.

## Analysis

We ran both operations on the aforementioned data set on 1, 2, 3, 4, and 5 workers in Google Cloud.
Below are our results.

|              | 1 Worker | 2 Workers | 3 Workers | 4 Workers | 5 Workers |
| ------------ | -------- | --------- | --------- | --------- | --------- |
| **Multiply** |  XXXX ms | XXXX ms   |   XXXX ms |   XXXX ms |   XXXX ms | 
| **PCA**      |  XXXX ms | XXXX ms   |   XXXX ms |   XXXX ms |   XXXX ms | 

As can be seen, ...
