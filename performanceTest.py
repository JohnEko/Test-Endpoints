import random
import json
import time
from confluent_kafka import Producer, Consumer, KafkaError
from configuration.config import BASE_URL, LOG


producer = Producer({'bootstrap.server': 'localhost:29092', 'broker.version.fallback': '0.9.0.0', 'api.version.request': False})

start_time = time.time()

try:
    for record in range(10):
        producer.produce("topicName", 'sas #{0}'.format(record))
except KeyboardInterrupt:
    pass
print("Process 1000 messages in {0: 2f} seconds".format(time.time()-start_time))

producer.flush(30)


settings = {
    'bootstrap.servers' : 'localhost:29092',
    'group.id' : 'mygroup',
    'client.id': 'client-1',
    'enable.auto.commit' : True,
    'session.timeout.ms':6000,
    'broker.version.fallback': '0.9.0.0',
    'api.version.request': False,
    'default.topic.config': {'auto.offset.reset':'smallest'}
}

consumer = Consumer(settings)
consumer.subscribe(['topicName'])
consumer_time = time.time()
msgcount = 0

try:
    while msgcount < 5:
        msg = consumer.poll(0.1)
        if msg is None:
            continue
        if msg.error():
            print('Error occured: {0}'.format(msg.error().str()))
            continue
        msgcount += 1
    print('Read {0} messages from {1}-{2} in {3:.2f} seconds'.format(msgcount, msg.topic(), msg.partition(),
                                                                     time.time()-consumer_time))
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    print('End to End time: {}'.format(time.time() - start_time))

