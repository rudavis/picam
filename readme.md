= My Pi Cam =
Simple example of using a PyQt UI to control a camera on Raspberry Pi.

== Running on Raspberry Pi ==
# sudo apt-get install python3 python3-pyqt5
# git clone https://github.com/rudavis/picam.git
# cd picam
# python3 main.py

=== Running on startup ===
# Edit this file:  nano /home/pi/.config/lxsession/LXDE-pi/autostart
# And add this line: @/usr/bin/python3 /home/pi/main.py
# reboot

== Running on OSX ==
# brew install python3
# brew install qt5
# brew install python3
# git clone https://github.com/rudavis/picam.git
# cd picam
# python3 main.py

= Reference = 
Big thanks to this tutorial:  https://www.baldengineer.com/raspberry-pi-gui-tutorial.html