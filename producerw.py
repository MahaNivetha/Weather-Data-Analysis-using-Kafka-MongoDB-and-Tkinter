import requests
from kafka import KafkaProducer
from json import dumps

# Replace 'YOUR_TOMORROW_IO_API_KEY' with your actual Tomorrow.io API key
TOMORROW_IO_API_KEY = 'fplDeaS6HfgARH8H2xzAmwtZtxU4CYe1'

# Kafka setup
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda K: dumps(K).encode('utf-8'))

# Location for which you want to fetch weather data (replace with your desired location)
latitude =  12.9716
longitude = 77.5946

# Tomorrow.io API endpoint
api_url = 'https://api.tomorrow.io/v4/weather/forecast'

# Tomorrow.io API parameters
params = {
    'location': f'{latitude},{longitude}',
    'apikey': TOMORROW_IO_API_KEY
}

# Make a request to the Tomorrow.io API
try:
    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    weather_data = response.json()

    # Send the weather data to Kafka topic
    producer.send('weatherTopic', weather_data)
    print('Weather data sent to Kafka topic.')
except requests.exceptions.RequestException as e:
    print(f'Error fetching weather data: {e}')

# Close the Kafka producer
producer.close()