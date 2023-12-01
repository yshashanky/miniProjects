# To add a 5-second delay after entering each message while sending them to the Kafka producer, you can utilize the time module in Python. Here's the modified code:

import subprocess
import time

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

# In this modified code, the time module is imported to enable the use of time.sleep(5) function, which introduces a 5-second delay.
# The loop that sends the messages to the Kafka producer now includes the time.sleep(5) line after writing each message to the producer's standard input. This ensures a pause of 5 seconds before sending the next message.
# Make sure to adjust the path, producer_command, messages, and other parameters to match your Kafka setup and the desired behavior.
