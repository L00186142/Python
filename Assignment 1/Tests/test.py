'''
Script: test.py
By: NM
Purpose: Testing that the connection for server and client are the same.
Date: 18NOV23

'''
# import sys
# Import the location of the master folder for this test to run
# sys.path.append(r"D:/IaC/Assignment1/L00186142")

import unittest

import Source.Network.Settings.udp as network

class TestUDPClientServer(unittest.TestCase):
    def test_server_address(self):
        # Access the server address from the network module
        actual_server_address = (network.UDP["SERVER_UDP_IPv4"], network.UDP["SERVER_PORT"])

        # Expected server address
        expected_server_address = ("127.0.0.1", 23)

        # Assert that the actual server address matches the expected address
        self.assertEqual(actual_server_address, expected_server_address)
    def test_client_address(self):
        # Access the server address from the network module
        actual_client_address = (network.UDP["CLIENT_UDP_IPv4"])

        # Expected server address
        expected_client_address = ("127.0.0.0") 

        # Assert that the actual server address matches the expected address
        self.assertEqual(actual_client_address, expected_client_address)
    
if __name__ == "__main__":
    unittest.main()

# Test Material to Revert back to the original
#     UDP = {
#     "SERVER_UDP_IPv4": '127.0.0.1',
#     "CLIENT_UDP_IPv4": '127.0.0.0',
#     "SERVER_PORT": 23
# }