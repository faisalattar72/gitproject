from pyspark.sql import  SparkSession
spark = SparkSession.builder.appName("intelli_pyspark").master("local").getOrCreate()
print("this is pyspark proj.")
df=spark.range(100)
print(df.sample(0.06).collect())
print("new_line")
