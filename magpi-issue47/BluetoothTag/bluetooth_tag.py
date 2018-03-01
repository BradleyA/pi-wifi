#/usr/bin/env python

import time
import bluetooth
from wakeonlan import 

phone = "98:03:D8:A6:7A:2A"

def search():         
    devices = bluetooth.discover_devices(duration=5, lookup_names = True)
    return devices

while True:        
    results = search()

    for addr, name in results:
        if addr == phone:
            wol.send_magic_packet('ff:ff:ff:ff:ff:ff') # PC to wake on LAN

    time.sleep(20)
