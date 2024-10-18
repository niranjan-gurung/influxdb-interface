#############################################################
#                                                           #
# contains methods to interact with influxdb cloud TSM (v2) #
#                                                           #
#############################################################

from influxdb_client import BucketRetentionRules
from influxdb_client.client.write_api import SYNCHRONOUS

from test_data.structured_data import Sensor
from connect_db import init_connection
import random

"""
Returns a list of all buckets
"""
def list_buckets():
    with init_connection() as client:
        buckets_str = []
        buckets_api = client.buckets_api()
        buckets = buckets_api.find_buckets_iter()

        for bucket in buckets:
            buckets_str.append(bucket.name)
            
        return buckets_str

"""
Create new bucket + define its retention,
"""
def create_db(bucket_name, bucket_ret_days):
    # string -> int
    ret_days = int(bucket_ret_days)
    
    # retention == how long DB will keep its data
    if ret_days == 0:
        bucket_ret_sec = None   # no expiration
        retention_rules = []
    else:
        # converts from days to seconds
        bucket_ret_sec = ret_days * 86400
        retention_rules = BucketRetentionRules(
            type="expire", 
            every_seconds=bucket_ret_sec)
    
    # establish connection to influxdb
    with init_connection() as client:
        buckets_api = client.buckets_api()
        
        # create bucket:
        bucket = buckets_api.create_bucket(
            bucket_name=bucket_name,
            retention_rules=retention_rules,
            org=client.org
        )
        return bucket

"""
Generate fake/dummy data for testing,
creates sensor data used in trains by default.
"""
def generate_data(bucket_name, row_amount):
    # used to change tag (from 101 - 105)
    counter = 0

    # return value..
    # used for debug
    sensor_data = []

    # establish connection to influxdb
    with init_connection() as client:
        for i in range(int(row_amount)):
            if i % 5 == 0:
                counter = 0
            counter += 1

            # prepare payload
            sensor = Sensor(
                'TLM010' + str(counter),            # tag
                round(random.uniform(5, 35), 2),    # temp
                round(random.uniform(30, 85), 2),   # hum
                random.randrange(100, 800),         # lux
                random.randrange(250, 1000),        # co2
                round(random.uniform(-1, 1), 3),    # acx
                round(random.uniform(-1, 1), 3),    # acy
                round(random.uniform(-1, 1), 3))    # acz
            
            print(sensor)
            sensor_data.append(sensor)

            write_api = client.write_api(write_options=SYNCHRONOUS)
            write_api.write(
                bucket=bucket_name, 
                record=sensor, 
                record_measurement_name="railData",
                record_tag_keys=["sensor_id"],
                record_field_keys=[
                    "temp", 
                    "hum", 
                    "lux", 
                    "co2", 
                    "acX", "acY", "acZ"])
            
        return sensor_data
            
    