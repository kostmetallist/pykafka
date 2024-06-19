import os

from kafka import KafkaConsumer

KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:29092')
KAFKA_TOPIC_TEST = os.environ.get('KAFKA_TOPIC_TEST', 'test')
# The version can be retrieved from within the kafka container:
# $ docker exec kafka kafka-topics --version
KAFKA_API_VERSION = os.environ.get('KAFKA_API_VERSION', '7.6.1')


if __name__ == '__main__':

    consumer = KafkaConsumer(
        KAFKA_TOPIC_TEST,
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        api_version=KAFKA_API_VERSION,
        auto_offset_reset='earliest',
        enable_auto_commit=True
    )

    for message in consumer:
        print(message.value.decode('utf-8'))
