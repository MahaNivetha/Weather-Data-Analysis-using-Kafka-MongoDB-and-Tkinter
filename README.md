# Weather Data Analysis using Kafka, MongoDB, and Tkinter

This project is a comprehensive solution for real-time weather data analysis, combining the strengths of Apache Kafka, MongoDB, and Tkinter. We aim to provide users with an efficient and user-friendly platform to stream, store, and analyze live weather data seamlessly.


Key Features:

Real-Time Streaming: Harness the power of Apache Kafka to stream live weather data from various sources, ensuring a continuous and up-to-date flow of information.
Efficient Data Storage: MongoDB, a robust NoSQL database, is employed for storing the streamed weather data. Its flexible and scalable nature facilitates easy data retrieval and management.
Advanced Analysis with Spark: Leverage Apache Spark's data processing capabilities to conduct in-depth analysis on the stored weather data, extracting valuable insights and trends.
User-Friendly Interface: The Tkinter-based graphical user interface provides an intuitive platform for users to interact with the analyzed data, visualize trends, and make informed decisions based on the weather information.
How to Use:

Setup Prerequisites: Ensure the installation of Apache Kafka, MongoDB, and required Python libraries.
Run Scripts: Execute the provided Python scripts (producerw.py, consumerw.py, visual.py) to initiate the data streaming, storing, and GUI functionalities.
Real-Time Analysis: Experience real-time weather data analysis through the Tkinter GUI, allowing users to visualize trends and patterns effortlessly.
Acknowledgments: We express gratitude to Tomorrow.io API, Apache Kafka, MongoDB, Apache Spark, Tkinter, and Matplotlib for their crucial contributions to this project.
Explore the Weather Data Analysis project and gain valuable insights into weather patterns, trends, and forecasts with ease!
## Prerequisites

Before running the application, ensure you have the following installed:

- Apache Kafka
- MongoDB
- Python 3
- Required Python libraries (requests, kafka-python, pymongo, tkinter, matplotlib)

Install Python libraries using:

```bash
pip install requests kafka-python pymongo matplotlib
```

## Kafka Setup

1. Start Zookeeper:

    ```bash
    bin/zookeeper-server-start.sh config/zookeeper.properties
    ```

2. Start Kafka Server:

    ```bash
    bin/kafka-server-start.sh config/server.properties
    ```

3. Create a Kafka topic:

    ```bash
    ./bin/kafka-topics.sh --create --topic weatherTopic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
    ```

4. Start Kafka Console Consumer:

    ```bash
    ./bin/kafka-console-consumer.sh --weather_topic --bootstrap-server localhost:9092 --from-beginning
    ```

## Producer Script (Python)

The `producerw.py` script fetches weather data using the Tomorrow.io API and sends it to the Kafka topic.

```bash
python producerw.py
```

## Consumer Script (Python)

The `consumerw.py` script consumes data from the Kafka topic and stores it in MongoDB.

```bash
python consumerw.py
```

## MongoDB Setup

1. Start MongoDB:

    ```bash
    mongod
    ```

2. Run Spark Shell with MongoDB connector:

    ```bash
    spark-shell --packages org.mongodb.spark:mongo-spark-connector_2.12:3.0.1
    ```

## Tkinter GUI (Python)

The `visual.py` script provides a Tkinter GUI to analyze weather data stored in MongoDB.

```bash
visual.py
```

## How it Works

1. The `producerw.py` script fetches weather data from the Tomorrow.io API and sends it to the Kafka topic.

2. The `consumerw.py` script consumes data from the Kafka topic and stores it in MongoDB.

3. The Tkinter GUI (`visual.py`) allows users to select an analysis option (e.g., temperature, humidity) and visualize the data using Matplotlib.

4. The MongoDB connector for Spark allows data analysis using Spark.

## Acknowledgments

- [Tomorrow.io API](https://www.tomorrow.io/weather-api/)
- [Apache Kafka](https://kafka.apache.org/)
- [MongoDB](https://www.mongodb.com/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Matplotlib](https://matplotlib.org/)

