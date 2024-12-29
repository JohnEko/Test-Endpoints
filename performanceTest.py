import random
import json
import time
from confluent_kafka import Producer, Consumer, KafkaError
from configuration.config import BASE_URL, LOG


producer = Producer({'bootstrap.server': 'localhost:29092', 'broker.version.fallback': '0.9.0.0', 'api.version.request': False})