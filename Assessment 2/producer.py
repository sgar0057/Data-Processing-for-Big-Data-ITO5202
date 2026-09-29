import argparse
import json
import time
from datetime import datetime, timezone

from kafka import KafkaProducer
from pyspark.sql import SparkSession


#create kafka producer
def create_producer(server):
    return KafkaProducer(
        bootstrap_servers=server,
        value_serializer=lambda x: json.dumps(x).encode("utf-8")
    )


def main():

    #settings
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input",
        default="data/stream_data.parquet"
    )

    parser.add_argument(
        "--topic",
        default="events"
    )

    parser.add_argument(
        "--bootstrap-server",
        default="localhost:9092"
    )

    # batch size is a parameter
    parser.add_argument(
        "--batch-size",
        type=int,
        default=500
    )

    args = parser.parse_args()

    if args.batch_size <= 0:
        raise ValueError("Batch size must be greater than 0.")

    #start spark and read the streaming data
    spark = (
        SparkSession.builder
        .appName("VicRoadsKafkaProducer")
        .master("local[*]")
        .getOrCreate()
    )

    df = spark.read.parquet(args.input)

    #convert spark rows to dictionary
    records = [row.asDict() for row in df.collect()]

    producer = create_producer(args.bootstrap_server)

    total_records = len(records)
    batch_number = 0

    try:

        #send the data in batches
        for start in range(0, total_records, args.batch_size):

            batch = records[start:start + args.batch_size]
            batch_number += 1

            #add the publication time to each record
            event_timestamp = datetime.now(timezone.utc).isoformat()

            for record in batch:
                record["event_timestamp"] = event_timestamp

            #send the batch as one json array
            producer.send(args.topic, batch)
            producer.flush()

            print(
                f"[{event_timestamp}] "
                f"Batch {batch_number} published | "
                f"records={len(batch)}"
            )

            #wait 5sec before sending the next batch
            if start + args.batch_size < total_records:
                time.sleep(5)

        print(
            f"Completed: {batch_number} batches, "
            f"{total_records} records."
        )

    finally:
        producer.close()
        spark.stop()


if __name__ == "__main__":
    main()