# Kafka-python system config -----------------
import sys
if sys.version_info >= (3, 12, 0):
    import six
    sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaConsumer
from json import loads
from time import sleep

def json_deserializer(encodedData):
    return loads(encodedData.decode('utf-8'))

consumer=KafkaConsumer(
    'first-topic',
    bootstrap_servers='',
    auto_offset_reset='earliest',
    value_deserializer=json_deserializer
)

for message in consumer:
    print('CONSUMER Message :',message.value)