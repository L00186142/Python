'''
Script: main.py
By: NM
Purpose: Script to run all the files together. The Server will be ran first then in a for loop the clients will be run together.
Date: 18NOV23

'''
# import the os module. https://www.geeksforgeeks.org/os-module-python-examples/
# import os

# # Set the working directory to the location of your scripts
# os.chdir(fr'D:\IaC\Assignment1\L00186142\Source')

# impoort the subprocess module https://www.datacamp.com/tutorial/python-subprocess
import subprocess
# import the time module
import time

# Configure the number of clients to run
num_clients = 3

# Function to run UDP server
def run_udp_server():
    subprocess.run(["python", "server.py"])

# Created a way to open all 3 clients in a function to run UDP client
def run_udp_client(client_script,sensor_id):
    subprocess.Popen(["python", client_script, sensor_id])


# Start the UDP server in a separate process
server_process = subprocess.Popen(["python", "server.py"])

# Pause to allow the server to start before clients
time.sleep(2)

# Start UDP clients in separate processes
for i in range(1, num_clients + 1):
    client_script = f"client{i}.py"
    run_udp_client(client_script, str(i))

# Wait for all clients to finish (Ctrl+C to stop)
server_process.wait()
