from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, LongType

# Initialize Spark session
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .getOrCreate()

# Define schema for incoming data
schema = StructType([
    StructField("timestamp", LongType(), True),
    StructField("value", LongType(), True)
])

# Read data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "real-time-data") \
    .load()

# Parse JSON data
parsed_df = df.selectExpr("CAST(value AS STRING) as json") \
    .select(from_json(col("json"), schema).alias("data")) \
    .select("data.*")

# Perform some transformations
transformed_df = parsed_df.withColumn("processed_value", col("value") * 2)

# Write data to console (for demonstration)
query = transformed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
