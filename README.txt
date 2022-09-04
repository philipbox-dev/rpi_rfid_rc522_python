to use this code first connect the rfid/nfc scanner to rpi using these pins:
3v3 - pin 1
rst - pin 22
gnd - pin 6
miso - pin 21
mosi - pin 19
sck - pin 23
sda - pin 24

Now we need to setup our workspace.

$ sudo raspi-config  
                     |-5 interfacing options/p4 SPI

$ sudo reboot
$ lsmod | grep spi

if spidev and spi_bcm2835 are in the list it is OK.

$ sudo apt-get update
$ sudo apt-get upgrade 
$ sudo apt-get install python3-dev python3-pip
$ sudo pip3 install spidev
$ sudo pip3 install mfrc522

Our workspace is Done.

 Now, for reading NFC/RFID card you need:

 $ sudo python3 read.py

 And for writing data:

 $ sudo python3 write.py


 ALL MADE BY PHILIPBOX.
 USE THE CODE FOR YOUR NEEDS.
