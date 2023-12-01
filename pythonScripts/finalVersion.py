# Executing simultaneously and displays a confirmation message once both processes are complete:

import subprocess
import time
import requests
from threading import Thread

# Code 1 - Kafka Producer
def run_kafka_producer():
    # Set the desired path
    path = 'C:/your/path'  # Replace with the desired path

    # Define the messages to be sent
    messages = [
        'Message 1',
        'Message 2',
        'Message 3'
    ]

    # Start Kafka producer
    producer_command = 'kafka-console-producer.bat --broker-list localhost:9092 --topic your_topic_name'
    producer_process = subprocess.Popen(producer_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=path)

    # Send messages to the producer with a 5-second delay
    for message in messages:
        producer_process.stdin.write(message.encode() + b'\n')
        producer_process.stdin.flush()
        time.sleep(5)  # 5-second delay

    # Terminate the producer process
    producer_process.terminate()


# Code 2 - API Calls
def run_api_calls():
    # First API Call
    url1 = 'https://api.example.com/endpoint1'
    params1 = {
        'param1': 'value1',
        'param2': 'value2'
    }
    headers1 = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer your_dummy_token'
    }

    response1 = requests.get(url1, params=params1, headers=headers1)

    if response1.status_code == 200:
        data1 = response1.json()
        # Extract path variables from the response
        variable1 = data1['variable1']
        variable2 = data1['variable2']
    else:
        print(f'Request failed with status code: {response1.status_code}')
        return

    # Second API Call
    url2 = f'https://api.example.com/endpoint2/{variable1}/{variable2}'
    params2 = {
        'query_param1': 'value1',
        'query_param2': 'value2'
    }
    headers2 = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer your_dummy_token'
    }

    response2 = requests.get(url2, params=params2, headers=headers2)

    if response2.status_code == 200:
        data2 = response2.json()
        # Process the response data from the second API call
        print(data2)
    else:
        print(f'Request failed with status code: {response2.status_code}')
        return


# Run Code 1 and Code 2 simultaneously
t1 = Thread(target=run_kafka_producer)
t2 = Thread(target=run_api_calls)

t1.start()
t2.start()

t1.join()
t2.join()

# Confirmation message
print("Both processes have completed.")

# In this combined code, two separate functions (run_kafka_producer and run_api_calls) are defined for Code 1 and Code 2, respectively. These functions are then executed simultaneously using threads (Thread) to run both processes in parallel.
# The join() method is used to wait for both threads to complete before displaying the confirmation message.
# Please make sure to replace the placeholder values such as the Kafka topic name, API endpoints, parameters, and headers with your actual values.
