from influxdb_client import InfluxDBClient, BucketRetentionRules, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.rest import ApiException

from connect_db import init_connection

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
        retention_rules = [BucketRetentionRules(
            type="expire", 
            every_seconds=bucket_ret_sec)]
    
    # establish connection to influxdb
    client = init_connection()
    buckets_api = client.buckets_api()

    try:
        # create bucket:
        bucket = buckets_api.create_bucket(
            bucket_name=bucket_name,
            retention_rules=retention_rules,
            org=client.org
        )
    except ApiException as e:
        print(f'Error create bucket: {e}')
        return False
    
    finally:
        client.close()

    return bucket

# generate fake/dummy data for testing..
def generate_data(bucket_name):
    # establish connection to influxdb
    client = init_connection()
    
    # prepare payload
    p = Point("test_measurement") \
        .tag("location", "Prague") \
        .field("temperature", 24.4) \
        
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket=bucket_name, record=p)