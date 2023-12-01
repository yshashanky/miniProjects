# To start a Kafka producer from a particular path through the CMD and then consume messages from Kafka, you can use the subprocess module in Python. Here's an example:

import subprocess

# Set the desired path
path = 'C:/your/path'  # Replace with the desired path

# Start Kafka producer
producer_command = 'kafka-console-producer.bat --broker-list localhost:9092 --topic your_topic_name'
producer_process = subprocess.Popen(producer_command, cwd=path)

# Consume Kafka messages
consumer_command = 'kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic your_topic_name --from-beginning'
subprocess.run(consumer_command, shell=True)

# Terminate the producer process
producer_process.terminate()


# In the above code, make sure to replace 'C:/your/path' with the actual path where the Kafka binaries are located.
# The producer_command variable specifies the command to start the Kafka producer using the kafka-console-producer.bat script. Adjust the --broker-list and --topic parameters to match your Kafka setup and desired topic name.
# The producer_process variable uses subprocess.Popen() to start the producer process. The cwd=path parameter sets the working directory to the specified path.
# The consumer_command variable specifies the command to consume Kafka messages using the kafka-console-consumer.bat script. Adjust the --bootstrap-server and --topic parameters as needed.
# The subprocess.run() function is called to execute the consumer command in the shell.
# Finally, the producer_process.terminate() method is used to terminate the producer process after consuming messages.
