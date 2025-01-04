# Kafka-python system config -----------------
import sys
if sys.version_info >= (3, 12, 0):
    import six
    sys.modules['kafka.vendor.six.moves'] = six.moves

from kafka import KafkaProducer
from json import dumps
from time import sleep

def json_visualizer(myData):
    return dumps(myData).encode('utf-8')

# Producer config
topic_name='first-topic'
producer=KafkaProducer(
    bootstrap_servers='',
    value_serializer=json_visualizer
)

producer.send(topic=topic_name, value='******************************************', partition=1)

for e in range(10):
    # This is a dictionary : key-value
    myMsg = {'I am a doctor and Eat an Apple daily : ':e}
    storage = producer.send(topic=topic_name, value=myMsg, partition=1)

    meta_data = storage.get(timeout=10)
    print('This is partition : ',meta_data.partition)
    sleep(1)    

