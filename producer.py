import json
import os
import random
import time

from kafka import KafkaProducer

KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost:29092')
KAFKA_TOPIC_TEST = os.environ.get('KAFKA_TOPIC_TEST', 'test')
# The version can be retrieved from within the kafka container:
# $ docker exec kafka kafka-topics --version
KAFKA_API_VERSION = os.environ.get('KAFKA_API_VERSION', '7.6.1')
MESSAGES_TO_SEND = 30


if __name__ == '__main__':

    producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVERS],
        api_version=KAFKA_API_VERSION
    )

    for i in range(MESSAGES_TO_SEND):
        producer.send(
            KAFKA_TOPIC_TEST,
            json.dumps({
                'message': f'Message #{i}'
            }).encode('utf-8')
        )
        time.sleep(random.randint(1, 5))

    producer.flush()
