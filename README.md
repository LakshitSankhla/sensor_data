# mqtt_sensorData
Simulation of some sensors used in a candy factory.
Publishers.py publishes the data from sensors and subscriber.py receives the data.
subscriber.py-->> if temperature is less than or greater than-------> Sends Error Message
                  if Humidity is greater then certain percentge for 5 mins------> Sends Error Email
                  Checks Status of machine
