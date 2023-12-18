# Readme
We needed to create a python script that has a UDP server and client that sends and receives data.
# Table of contents
- [Description](#description)
- [Table of contents](#table-of-contents)
- [UDP Server](#udp-client)
- [UDP Client](#udp-client)
- [Functions](#functions)
- [How to Run](#how-to-run)
- [Documentation](#documentation)

# Description
This assignment is a project that monitors the temperature, ID and timestamp of multiple sensors (Clients) then it sends packets back to the user (Server). Started with stating the Server IP address and port and client IP address. From there we created a UDP server that was listening for incoming packets from clients. Then created one UDP client to test that the client could send a packet and the server could receive one aswell. Started small by sending and receiving a message so that I knew the connection would work then built from there. 

Later decided to build up the communication so I sent temperature, timestamp and sensor number data as I knew I would be building 3 clients. Later I needed to send the data to a file so I decided on text files. In the server file, I created an if statement to determine whether the sensor was a certain number then sent data to that file and printed it out to the console. 

With each time testing that the communication was good, the project built to a point where there was 2 much code on the server file but for now it was okay. 

I knew I would need to create functions to strip down the code so I designed it to send the data of each sensor to its relevant counterpart. Later I would strip back the under 5 and over 30 to put them into functions aswell. 

In the advanced part of the project, we were tasked to print out an alert when the temperature was over 30 and under 5. With this in mind, I decided to print out an alert to screen and design 2 files to send the data out of each.


### UDP Server
A UDP Server is a program that uses User Datagram Protocol to talks to clients. UDP will listen on a certain Port then send and receive packets. The UDP server will listen on an IP address and port from clients to receive packets then process the data inside. 

1. This will run first to open a port for connection.
2. Can accept many client’s packets.
3. Waits for the client to send data.

### UDP Client
A UDP Client sends packets to the server but has to wait until the server is started. It has to be on the correct address or the packet won’t be sent. 

1. Waits for the server.
2. Sends packets.
3. Can only handle one server UDP connection.

### Functions
Designed 3 functions in the server.py to print out data to certain files. 
1. write_sensor_data
This function sends information to its own sensor number. 3 sensor files have been created at the beginning of the file. The information is appended to the file so data won’t be overwritten.

2. write_temperature_over_30
This function sends information to the file if the temperature is equal or over 30 degrees with the sensor number and timestamp.

3. write_temperature_under_5
Similar to the over_30 function, this function will write out data to a file that is under or equal to 5 degrees with sensor number and timestamp.

### How to Run
There is a more detailed how to run in the howToRun.md inside the Documentation folder but for now, in the directory of Source folder.

```python
python main.py
```

## Documentation 
In this folder we have a few small markdown files that outline the project in a bit more details. The files are as follows 
1. conclusion
2. howToRun
3. question
4. references
5. structure
6. testing

