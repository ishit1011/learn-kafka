from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Produce a message
producer.produce('test-topic', key='key1', value='Hello Kafka!', callback=delivery_report)

# Wait for all messages to be delivered
producer.flush()
