# Kafka-python system config -----------------
import sys
if sys.version_info >= (3, 12, 0):
    import six
    sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaProducer
from json import dumps
from time import sleep

def json_serializer(myData):
    return dumps(myData).encode('utf-8')

topic_name='first-topic'
producer= KafkaProducer(
    bootstrap_servers='',
    value_serializer=json_serializer
)

# Storing in random partition in multiple partitions in a topic
for e in range(10):
    data={'This message :':e}
    print(data)
    storage = producer.send(
        topic=topic_name,
        value=data)
    
    # Get partition and offset from RecordMetadata
    record_metadata = storage.get(timeout=10)
    print("Message stored in partition: ",record_metadata.partition)
    
    sleep(1)