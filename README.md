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

### 4. Run the producer

Activate the project environment:

conda activate ITO5202

Navigate to the Assessment 2 directory:

cd "Assessment 2"

Run the producer:

python producer.py --batch-size 500

The batch size can be changed like this:

python producer.py --batch-size 100

The producer publishes batches to the Kafka `events` topic
