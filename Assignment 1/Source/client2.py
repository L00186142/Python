'''
Script: client2.py
By: NM
Purpose: UDP Client for sensor 2 so it can send packets to the server.
Date: 18NOV23

'''
# Import the 'socket' module
import socket
# Import the 'time' module
import time
# Import the 'random' module
import random
# Import the 'udp' module from the 'Network.settings' package
import Network.Settings.udp as settings
# Import the 'datetime' module for timestamp creation
from datetime import datetime

# Retrieve the server's IPv4 address and port from the 'settings' module
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]

# Print client information
# print(f'This is the UDP client, it will try to connect to a server at {UDP_IP}:{UDP_PORT} in the settings file.')
# print('This script has error handling.')
# print('This is Sensor 2.')
# Start an infinite loop to try to connect
while True:
    # Create a UDP socket using the socket module
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # Set the sensor ID to '2'
            sensor_id = "2"
            # Simulated temperature reading with random number generator
            temperature = int(random.uniform(-5, 40)) 
            # Get the current timestamp in a certain format 
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formatted timestamp
            # Create a string with sensor ID, Timestamp and temperature 
            data = f"{sensor_id},{timestamp},{temperature}"
            # Encode the data from string into bytes
            message = data.encode('utf-8')
            # Send the data to the Server
            s.sendto(message, (UDP_IP, UDP_PORT))
            # Print the data to the console
            print(f"Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}\n")
            # Pause and Send data every 5 seconds
            time.sleep(10)  
        except Exception as e:
            # Handle exception and print it error message
            print(f"An error of type {type(e).__name__} occurred: {e}")

