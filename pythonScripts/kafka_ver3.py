# If you want to modify the previous code to accept the message input from an array of messages instead of user input, you can update the code as follows:

import subprocess

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

# Send messages to the producer
for message in messages:
    producer_process.stdin.write(message.encode() + b'\n')
    producer_process.stdin.flush()

# Terminate the producer process
producer_process.terminate()

# In this modified code, the messages list contains the messages that you want to send to the Kafka producer. You can modify the list and add or remove messages as needed.
# The rest of the code remains the same as before. The Kafka producer is started using the subprocess.Popen() function, and the messages are sent to the producer using a loop. Each message from the messages list is encoded as bytes and written to the producer's standard input using producer_process.stdin.write(). The producer_process.stdin.flush() method ensures that each message is immediately sent to the producer.
# Finally, the producer_process.terminate() method is used to terminate the producer process after sending all the messages.
# Make sure to adjust the path, producer_command, and other parameters to match your Kafka setup.
