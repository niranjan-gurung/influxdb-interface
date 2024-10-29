from influxdb_client import InfluxDBClient

from dotenv import load_dotenv
import os

# influx api token, url, org..
load_dotenv()

url = os.getenv('URL')
token = os.getenv('INFLUX_TOKEN')
org = os.getenv('ORG')

# establish connection to influxdb
def init_connection():
    client = InfluxDBClient(
        url=url,
        token=token,
        org=org
    )
    return client