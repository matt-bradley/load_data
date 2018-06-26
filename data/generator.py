import datetime

from time import sleep
from random import randint
from elasticsearch import Elasticsearch
from Timer import RepeatedTimer


def pushdata():
    load = {
        'train': 41,
        'carriage': {
            1: randint(1, 10),
            2: randint(1, 20),
            3: randint(1, 30),
            4: randint(1, 50),
            5: randint(1, 40),
            6: randint(1, 50),
            7: randint(1, 20),
            8: randint(1, 15),
        }
    }

    # datetimes will be serialized
    es.index(index="carriage-load", doc_type="carriage-type", body={"data": load, "timestamp": datetime.datetime.now()})
    # but not deserialized
    print load


print  datetime.datetime.now()
# by default we connect to localhost:9200
es = Elasticsearch(host='elasticsearch:9200')

es.indices.create(index='carriage-load', ignore=400)

rt = RepeatedTimer(5, pushdata)  # it auto-starts, no need of rt.start()
try:
    sleep(3000)
finally:
    print datetime.datetime.now()
    rt.stop()
