# Real-Time Data Pipeline with Apache Kafka and Apache Spark

## Description
This project demonstrates a real-time data pipeline using Apache Kafka for data ingestion and Apache Spark for real-time data processing. The pipeline ingests data from a Kafka producer, processes it using Spark Streaming, and writes the results to the console.

## Architecture
The architecture of the real-time data pipeline includes:
1. **Kafka Producer**: Generates and sends data to a Kafka topic.
2. **Kafka Broker**: Receives and stores data from the producer.
3. **Spark Streaming Application**: Consumes data from the Kafka topic, processes it in real-time, and writes the results to the console or other storage solutions.

## Prerequisites
- Python 3.x
- Apache Kafka
- Apache Spark
- PostgreSQL (optional, for data storage)
- Required Python libraries: `kafka-python`, `pyspark`

## Installation

### Kafka Installation
1. Download and extract Kafka:
   ```sh
   wget https://downloads.apache.org/kafka/2.8.0/kafka_2.13-2.8.0.tgz
   tar -xzf kafka_2.13-2.8.0.tgz
   cd kafka_2.13-2.8.0

  
