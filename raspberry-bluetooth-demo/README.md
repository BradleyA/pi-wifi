# raspberry-bluetooth-demo

This demo shows how to setup a simple bluetooth server in a Raspberry Pi so an Android Phone can connect to it.

##Prerequisites
This demo assumes:
* basic Linux (*nix also works too) command line knowledge
* Python knowledge

This demo was tested using the Raspberry Pi 3 that comes with pi-bluetooth pre-loaded and working 'out of the box'. If you are using an older version set up pi-bluetooth before following this demo, multiple resources can be found online. Depending on your setup the following command should work:

```
sudo apt-get install pi-bluetooth
```

This demo uses Bluez, Linux's Bluetooth protocol stack, we'll be using [PyBluez](https://github.com/karulis/pybluez), a Python API for accesing the bluetooth resources using the bluez protocol.

##Installation

install bluez
```
sudo apt-get install bluetooth bluez
```

install pyBluez
```
sudo apt-get install bluez python-bluez
```

##Setup your Raspberry Pi

Make your device discoverable
```
sudo hciconfig hci0 piscan
```
Configure your device name
```
sudo hciconfig hci0 name 'Device Name' [change your device name to something else you fancy]
```

##Scanning for devices
run the inquiry example:
```
sudo python /usr/share/doc/python-bluez/examples/simple/inquiry.py
```

The example may also be found [here](https://github.com/karulis/pybluez/blob/master/examples/simple/inquiry.py).


##Running the Bluetooth Server
run the rfcomm-server example:
```
sudo python /usr/share/doc/python-bluez/examples/simple/rfcomm-server.py
```

The example may also be found [here](https://github.com/karulis/pybluez/blob/master/examples/simple/rfcomm-server.py). After running the script the server will be waiting for an incoming connection.

##Connecting from an Android Phone
There are several applications in the Google Play Store for bluetooth connectivity that may work. We'll be using [BlueTerm](https://play.google.com/store/apps/details?id=es.pymasde.blueterm&hl=en) as it supports the RFCOMM bluetooth protocol.

__Steps:__  
1. Download [BlueTerm](https://play.google.com/store/apps/details?id=es.pymasde.blueterm&hl=en)  
2. Scan for devices, if you've done everything correctly the Raspberry Pi should show up  
3. Connect  
4. Success! Send messages back and forth!  

##Credits
This demo would not have been possible thanks to the following posts and online resources:
* [Android Linux / Raspberry Pi Bluetooth communication](http://blog.davidvassallo.me/2014/05/11/android-linux-raspberry-pi-bluetooth-communication/)  
* [Raspberry Pi 3 Bluetooth Setup](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=138145)  

Although this repo intends to be a summary of these resources, if you are stuck it might be useful to check them out.

##Known Issues

```
Traceback (most recent call last):
  File "/usr/share/doc/python-bluez/examples/simple/rfcomm-server.py", line 20, in <module>
    profiles = [ SERIAL_PORT_PROFILE ], 
  File "/usr/lib/python2.7/dist-packages/bluetooth/bluez.py", line 176, in advertise_service
    raise BluetoothError (str (e))
bluetooth.btcommon.BluetoothError: (2, 'No such file or directory')
```
__Possible fixes__
* make sure you are using sudo when running the python script
* make sure you have the serial profile loaded. [How to enable the serial profile](https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=133263).
* Yor own fix? Make a pull request!

##Important Note!
If something didn't work for you, you had to implement a weird fix or hack, or you think something could be explained better (maybe you found a typo, missing comma, or some weird wording (this is very much likely)) feel free to make a pull request!
