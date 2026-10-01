# Data Processing for Big Data ITO5202

student_id: '33759839'

unit: 'ITO5202 TP5-26'

selected_dataset: 'vic_road_crash_data.csv'

source: 'https://opendata.transport.vic.gov.au/dataset/victoria-road-crash-data/resource/5df1f373-0c90-48f5-80e1-7b2a35507134'


## Assignment 2: Reproducing Kafka Producer

Before running the producer, start ZooKeeper and Kafka using the following commands.

### 1. Start ZooKeeper

docker start zookeeper

### 2. Start Kafka

docker start kafka

### 3. Verify Kafka is running

docker ps

Kafka should be listed as a running container.

Verify that Kafka is accepting connections:

nc -vz localhost 9092

Expected output:

Connection to localhost port 9092 [tcp/*] succeeded!

### 4. Start Jupyter notebook with the Spark/Kafka connecter 
run the following: 
PYSPARK_SUBMIT_ARGS="--driver-class-path $HOME/.ivy2.5.2/jars/org.apache.kafka_kafka-clients-3.9.2.jar:$HOME/.ivy2.5.2/jars/org.apache.spark_spark-sql-kafka-0-10_2.13-4.2.0.jar:$HOME/.ivy2.5.2/jars/org.apache.spark_spark-token-provider-kafka-0-10_2.13-4.2.0.jar:$HOME/.ivy2.5.2/jars/org.apache.commons_commons-pool2-2.13.1.jar --packages org.apache.spark:spark-sql-kafka-0-10_2.13:4.2.0 pyspark-shell" jupyter notebook

### 5. Run the assessment 2 notebook Part B
1. Create a local Spark session
2. Connect to Kafka topic events
3. Read Kafka message values as JSON
4. Parse the JSON using schema
5. Explode JSON array into individual crash records
6 Converts event_timestamp into a Spark timestamp
7. Load the persisted model from models/a2_model
8. Apply the complete model pipeline to the streaming data
9. Perform a one minute window aggregation by predicted class
10. Write completed window results to output/predictions in Parquet format

The streaming query is named vicRoads_prediction_windows and uses output/predictions for the output and checkpoints/predictions for Spark checkpointing.

### 6. Run the producer

Activate the project environment:

conda activate ITO5202

Navigate to the Assessment 2 directory:

cd "Assessment 2"

Run the producer:

python producer.py --batch-size 500

The batch size can be changed like this:

python producer.py --batch-size 100

The producer publishes batches to the Kafka `events` topic
