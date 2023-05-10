# jumble-iot-device
 Software to track ice cream truck, temperature, humidity , location and send via rest APi

First phase is to initially test each of the hardware individually before integrating with the whole project followed by creating the flask web api.

Main c code to integrate all the sensors would be in main_driver.ino

# Program Setup

## Setup

### Create virtual env

Mac
>python3 -m venv venv

Windows 
>py -3 -m venv venv

Install libraries
>pip install -r requirements.txt 

### Flask Specific Setup locally

Sometimes flask is confused and doesn't know what it wants, so tell it
>export FLASK_APP=app.py



Database migrations

Intialise database
>flask db init    

Perform Migrations
```
flask db migrate -m 'add status'
flask db upgrade
```
#  Hardware Setup
This includes sites used for checking the pin setup and possible links to library to allow reproduction in case

## Tempeature and Humidity Sensor (DHT11)

### Library setup 
install directly from library manager

### Guide information

[DHT11 setup guide](https://www.electronicwings.com/sensors-modules/dht11) 

### Pin setup
1. vcc - 5v 
2. gnd - gnd
3. digital - pin 2




## GPS module (NEO8m Module)

### Library setup 

install library via Github repo
```
https://github.com/mikalhart/TinyGPSPlus
```

### Pin setup
1. vcc - 5v 
2. gnd - gnd
3. rxd - pin3
4. txd - pin4 


## Light sensor (TSL2561)

### Guide information

[TSL2561 setup guide](https://electropeak.com/learn/interfacing-tsl2561-luminosity-sensor-with-arduino/#:~:text=The%20TSL2561%20Luminosity%20Sensor%20Breakout,datasheet%20of%20this%20module%20here.)
 
### Library setup 
install library via Github repo
```
https://github.com/mikalhart/TinyGPSPlus
```

### Pin setup
1. vcc - 5v 
2. gnd - gnd
3. scl - Analog5
4. sda - Analog4 
