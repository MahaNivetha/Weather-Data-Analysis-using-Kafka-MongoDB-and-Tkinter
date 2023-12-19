from kafka import KafkaConsumer
import json
from pymongo import MongoClient

# MongoDB setup
mongo_client = MongoClient('localhost', 27017)
db = mongo_client['weather_db']
collection = db['weather_collectionss']

# Kafka consumer setup
consumer = KafkaConsumer(
    'weatherTopic',
    group_id='weather-group',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

try:
    # Consume and store messages in MongoDB
    for message in consumer:
        weather_data = message.value

        # Insert data into MongoDB collection
        collection.insert_one(weather_data)

        print('Weather data stored in MongoDB:', weather_data)

except KeyboardInterrupt:
    print("Consumer interrupted. Closing gracefully.")

finally:
    # Close the Kafka consumer and MongoDB connection
    consumer.close()
    mongo_client.close()