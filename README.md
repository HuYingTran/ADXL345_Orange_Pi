# ADXL345_Orange_Pi

Connecting to i2c-1 interface on orange pi
In menuconfig need to enable i2c-1 interface

![alt text](image/image-1.png)
![](image/hardware2.jpg)
Sudo orangepi-config\
->system -> hardware->reboot

![alt text](image/image-2.png)

Install i2c tools
sudo apt-get install i2c-tools

search for i2c devices on channels
```
i2cdetect -y 1
i2cdetect -y 2
```
i2c address of ADXL234 is 0x53

![alt text](image/image.png)

Install python pip tool
```
sudo apt install python3-pip
```
Install smbus for bus communication with i2c device
```
sudo pip install smbus
```
RUN code
```
python3 read_ADXL345.py
```

![](image/hardware.jpg)