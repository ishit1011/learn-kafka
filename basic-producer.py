# Kafka-python system config -----------------
import sys
if sys.version_info >= (3, 12, 0):
    import six
    sys.modules['kafka.vendor.six.moves'] = six.moves

# Kafka-code for manually generating messages as producer ---------------------------
from kafka import KafkaProducer
from json import dumps
from time import sleep

def json_serializer(myData):
    return dumps(myData).encode('utf-8')

topic_name = 'topic-hello-world'
producer = KafkaProducer(
    bootstrap_servers='',
    value_serializer=json_serializer
)

for e in range(100):
    message = {'This is message number : ':e}
    print(message)
    producer.send(
        topic=topic_name,
        value=message
    )
    sleep(0.5)