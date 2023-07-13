from pyspark import * 

## Main functionality

def main(sc):

 rdd = sc.parallelize(range(1000), 10)
 print rdd.mean()

if __name__ == "__main__":

    conf = SparkConf().setAppName("submitme")
    sc   = SparkContext(conf=conf)
    main(sc)
