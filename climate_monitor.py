

from datetime import datetime
from functools import partial

from climate_utils import read_stats, reading_storer
from climate_utils import load_timestamp, dump_timestamp, timestamp_format


def run_climate_monitor(readings, store):
    """
    """
    
    for stats in readings:
        reading = {
            "timestamp": dump_timestamp(datetime.utcnow()),
            "sensor_id": "A",
            "location": None
        }
        reading.update(stats)
        
        store(reading)
        
        
        
        
if __name__ == "__main__":

    #output_file = "/home/pc/climatedata.log"
    output_file = "/Users/dhahne/Development/pianoclimate/climatedata.log"
    
    store = partial(reading_storer, store_location=output_file)
    readings = read_stats(None, None)
    run_climate_monitor(readings, store)
