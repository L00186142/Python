# Question for the Project

A farmer needs help!

In several outbuildings, he needs to monitor temperature in several different locations. He has been quoted an astronomical price for a professional system. He has asked me to help. I can add Raspberry Pi Zero-W (RPi) for a few Euros each. I can put 1-wire sensors on them for less than a Euro each. Job done! I need a hand. I need you to write me a simulator to demonstrate this. Write three UDP clients which will unicast a single temperature to a server, with a time stamp and a sensor ID.

Write a server to receive this data and save it in separate logfiles.

## Extra Marks
It would be a real bonus if we can alert the farmer when temperature is <5c or >30c