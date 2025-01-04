# Kafka-python system config -----------------
import sys
if sys.version_info >= (3, 12, 0):
    import six
    sys.modules['kafka.vendor.six.moves'] = six.moves

# Kafka-code for manually generating messages as producer ---------------------------
from kafka import KafkaProducer
from json import dumps
from time import sleep

topic_name = 'topic-hello-world'
producer = KafkaProducer(
    bootstrap_servers='',
    value_serializer=lambda v: dumps(v).encode('utf-8')
)

for e in range(100):
    message = {'This is message number : ':e}
    print(message)
    producer.send(
        topic=topic_name,
        value=message
    )
    sleep(5)