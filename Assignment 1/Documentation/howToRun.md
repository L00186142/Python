# How to Run
There are 2 ways that we can get this assignment to run. 
1. We have to run the server and client scripts manually in 4 different cmd lines. 
2. We can run the main script that will all of them simultaneously.

## 1. Running Sever and Clients
### Running the Server

1. Make sure the server IP and port are correctly configured in the 'Network.Settings.udp' module.
2. Run the server script to start listening for sensor data in a cmd prompt.

```python
python server.py
```
### Running the Clients

1. Similar to Server, Make sure the client IP are correctly configured in the 'Network.Settings.udp' module.
2. Run all the client scripts to ostart sending packets of the sensor data in different cmd prompts.

```python
python client1.py

python client2.py

python client3.py
```

## 2. Running Main
### Running Main

1. Make sure the server IP and port then the client IP are correctly configured in the 'Network.Settings.udp' module.
2. Run the main script that will run the server then the clients in a cmd prompt.

```python
python main.py
```
