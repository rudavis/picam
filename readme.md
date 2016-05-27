# My Pi Cam
Simple example of using a PyQt UI to control a camera on Raspberry Pi.

## Running on Raspberry Pi
1. sudo apt-get install python3 python3-pyqt5
2. git clone https://github.com/rudavis/picam.git
3. cd picam
4. python3 main.py

### Running on startup
1. Edit this file:  nano /home/pi/.config/lxsession/LXDE-pi/autostart
2. And add this line: @/usr/bin/python3 /home/pi/main.py
3. reboot

## Running on OSX
1. brew install python3
2. brew install qt5
3. brew install python3
4. git clone https://github.com/rudavis/picam.git
5. cd picam
6. python3 main.py

# Reference 
Big thanks to this tutorial:  [https://www.baldengineer.com/raspberry-pi-gui-tutorial.html]