from configparser import ConfigParser
from kafka import KafkaConsumer, KafkaProducer
import json
from sqlalchemy import create_engine

def config(filename, section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db


def get_consumer(topic):
    consumer = KafkaConsumer(topic,
                             bootstrap_servers=['13.235.245.66:9092'],
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))
    return consumer


def get_producer():
    producer = KafkaProducer(bootstrap_servers=['13.235.245.66:9092'],
                             value_serializer=lambda x:
                             json.dumps(x).encode('utf-8'))
    return producer
