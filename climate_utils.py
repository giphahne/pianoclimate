
# import <dht stuff>
import random
import time
import json

timestamp_format = '%Y-%m-%d %H:%M:%SZ'


def fake_read_stats(sens_type, pin):
    """
    """


    while True:
        time.sleep(random.uniform(0.1, 1.8))        
        yield {
            "temp": random.randint(18, 25),
            "humd": random.randint(39, 43)
        }

    
def fake_store_reading(reading):
    """
    """
    print(reading)
    
    
def read_stats(sens_type, pin):
    """
    """
    return fake_read_stats(sens_type, pin) 
    

def reading_storer(reading, store_location):
    """
    """
    return fake_store_reading(reading)


def load_timestamp(timestamp_string):
    if isinstance(timestamp_string, datetime):
        return timestamp_string
    
    return pytz.timezone('UTC').localize(
        datetime.strptime(timestamp_string, timestamp_format)
    )


def dump_timestamp(timestamp):
    return timestamp.strftime(timestamp_format)


