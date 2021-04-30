#!/usr/bin/python3

switchport = {"operational_status": "up", "administrative_status": "down"}

if switchport["operational_status"] == "up" and switchport["administrative_status"] == "up":
    print("Port is good to go!")
else:
    if switchport["operational_status"] == "down":
        print("Check administrative status and cabling.")
    elif switchport["administrative_status"] == "down":
        print("Port needs to be administratively enabled.")
