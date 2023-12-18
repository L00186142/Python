'''
Script: server.py
By: NM
Purpose: UDP Server to recieve packets off the clients then send out the data to files.
Date: 18NOV23
Information: Functions have been added to this file to meet the structure of the project and tidy up certain length of the project.
'''
# Import the 'socket' module
import socket
# import the os module
import os
# Import the 'udp' module from the 'Network.settings' package
import Network.Settings.udp as settings

# Retrieve the server's IPv4 address, port, and buffer size from the 'settings' module
UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

# Specify the folder names
OUTPUT_FOLDER = "Output"

# Create the output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

LOG_FILE = os.path.join(OUTPUT_FOLDER, "sensor_logs.txt")
ALERT_FILE_5 = os.path.join(OUTPUT_FOLDER, "alertsUnder5.txt")
ALERT_FILE_30 = os.path.join(OUTPUT_FOLDER, "alertsabove30.txt")
# Create the 3 sensor files
SENSOR_FILE_PATHS = {
    '1': os.path.join(OUTPUT_FOLDER, 'sensor_1.txt'),
    '2': os.path.join(OUTPUT_FOLDER, 'sensor_2.txt'),
    '3': os.path.join(OUTPUT_FOLDER, 'sensor_3.txt'),
}

# Print server information to the console
print(f'This is the UDP server, it will open a port at {UDP_IP}:{UDP_PORT} and begin listening')
print(f'Make sure the actual server IP address matches {UDP_IP} in the settings file')
print(f'There are a number of files being saved. Alerts, Over 30 degrees, Under 5 degrees, each sensor(1-3) and an overall logfile')
print('This script has error handling.')

# Function that will Print out to files, for each sensor.
def write_sensor_data(sensor_id, timestamp, temperature):
    # Get the file path based on sensor_id
    sensor_file_path = SENSOR_FILE_PATHS.get(sensor_id)

    if sensor_file_path:
        # Write data to the specified file
        with open(sensor_file_path, "a") as file:
            file.write(f"Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}\n")
    else:
        print(f"Error: Invalid sensor_id {sensor_id}")

# Function if temperature is over 30 to print data out to log file
def write_temperature_over_30(sensor_id, timestamp, temperature):
    # Add the alert temperature text 
    if temperature > 30:
        alert_message = f"ALERT: Sensor ID {sensor_id} reports temperature above 30°C: {temperature}°C\n"
        print(alert_message)
        with open(ALERT_FILE_30, "a") as file:
            file.write(f"Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}\n")

# Function if temperature is over 30 to print data out to log file
def write_temperature_under_5(sensor_id, timestamp, temperature):
    if temperature < 5:
        # Add the alert temperature text 
        alert_message = f"ALERT: Sensor ID {sensor_id} reports temperature below 5°C: {temperature}°C\n"
        print(alert_message)
        # Append the alert message to the alert file. 'a' means append
        with open(ALERT_FILE_5, "a") as file:
            file.write(f"Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}\n")

# Create a UDP socket using the 'socket' module
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    try:
        # Enable broadcast mode for the socket
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Bind socket to IP address and port
        s.bind((UDP_IP, UDP_PORT))
        print('Listening on', UDP_IP)
        # Start the infinite loop to continue listening for packets
        while True:
            # Recieve packets from the socket
            data, addr = s.recvfrom(BUFFER_SIZE)
            # Decode from bytes to string
            data = data.decode()
            # Split the received data into components using ',' as the delimiter
            sensor_id, timestamp, temperature = data.split(',')
            # Convert temperature to a integer for comparison
            temperature = int(temperature)
            # Function to print out data of each sensor.
            write_sensor_data(sensor_id, timestamp, temperature)
            # Fuunction to Write out to below to 5 degrees file with data. 
            write_temperature_under_5(sensor_id, timestamp, temperature)
            # Function Write out to above to 30 degrees file with data. 
            write_temperature_over_30(sensor_id, timestamp, temperature)
            print(f"Received data from Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}°C\n")
            # Writing out all sensors data to file. 
            with open(LOG_FILE, "a") as file:
                file.write(f"Sensor ID: {sensor_id}, Timestamp: {timestamp}, Temperature: {temperature}\n")
    # Handle exceptions and print an error message   
    except Exception as e:
        print(f"An error of type {type(e).__name__} occurred: {e}")
    except IOError as err:
        print(f"IOError was {err}")
    except EOFError as err:
        print(f"End of file error was {err}")
    except OSError:
        print("OS Error")
    except:
        print("General Error")