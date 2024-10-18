from dataclasses import dataclass

# structure for data payload
# some example test data

@dataclass
class Sensor:
    # tags
    sensor_id: str

    # fields
    temp: float
    hum: float
    lux: int
    co2: int
    acX: float
    acY: float
    acZ: float

# todo:
class Country:
    pass

class Car:
    pass