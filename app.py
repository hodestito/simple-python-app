import csv
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['kafka:9092'])

fieldnames = ("Data","Num1","Num2","Cor","Final")

f = open('example.csv', 'r')
reader = csv.DictReader(f, fieldnames)

for row in reader:
    # Parse CSV into JSON  
    out = json.dumps(row)
    # Convert do bytes
    msg = out.encode()
    # Send message to Kafka topic
    future = producer.send('csv_topic', msg)    
    future.get(timeout=10)
    # Print message to console
    print(msg)
