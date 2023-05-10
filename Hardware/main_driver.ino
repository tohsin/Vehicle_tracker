#include <Wire.h>
#include "TSL2561.h"
#include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT11


class Data{
private:
  TSL2561 tsl;
  DHT dht;
  
  uint16_t irValue;
  uint16_t fullValue;
  uint16_t visibleValue;
  uint32_t luxValue;
  bool tslFound;
   
  float temperatureValue;
  float humidityValue;
  float heatIndexValue;
  bool dhtFound;
  
public:
  Data() : tsl(TSL2561_ADDR_FLOAT), dht(DHTPIN, DHTTYPE), tslFound(false), dhtFound(false){}

 
  void setupTSL() {
    if (tsl.begin()) {
      tslFound = true;
      Serial.println("Found sensor");
    } else {
      Serial.println("No sensor found");
    }

    tsl.setGain(TSL2561_GAIN_16X);
    tsl.setTiming(TSL2561_INTEGRATIONTIME_13MS);
  }

  void setupDHT() {
    dht.begin();
    dhtFound = true;
    Serial.println("Found temperature sensor");
  }

  
  void readTSLData() {
    if (!tslFound) {
      return;  // Skip reading sensor data if the sensor was not found
    }

    uint32_t lum = tsl.getFullLuminosity();
    irValue = lum >> 16;
    fullValue = lum & 0xFFFF;
    visibleValue = fullValue - irValue;
    luxValue = tsl.calculateLux(fullValue, irValue);
  }

  void readDHTData() {
    float h = dht.readHumidity();
    float t = dht.readTemperature();
    if (isnan(h) || isnan(t)) {
        Serial.println("Failed to read from DHT sensor!");
        dhtFound = false;
        return;
      }

    temperatureValue = t;
    humidityValue = h;
    heatIndexValue = dht.computeHeatIndex(t, h);
  }

  void printTSLData() {
    if (!tslFound) {
      Serial.println("Sensor not found");
      return;  // Skip printing sensor data if the sensor was not found
    }

    Serial.print("IR: "); Serial.print(irValue); Serial.print("\t\t");
    Serial.print("Full: "); Serial.print(fullValue); Serial.print("\t");
    Serial.print("Visible: "); Serial.print(visibleValue); Serial.print("\t");
    Serial.print("Lux: "); Serial.println(luxValue);
  }

  void printDHTData() {
    if (!dhtFound) {
      Serial.println("Temperature sensor not found");
      return;  // Skip printing sensor data if the sensor was not found
    }

    Serial.print("Temperature: "); Serial.print(temperatureValue); Serial.print("°C\t");
    Serial.print("Humidity: "); Serial.print(humidityValue); Serial.print("%\t");
    Serial.print("Heat Index: "); Serial.print(heatIndexValue); Serial.print("°C\n\n");
  }
  

 void readData() {
    readTSLData();
    readDHTData();
  }

  void printData() {
    printTSLData();
    printDHTData();
  }



  uint16_t getIRValue() const {
    return irValue;
  }

  uint16_t getFullValue() const {
    return fullValue;
  }

  uint16_t getVisibleValue() const {
    return visibleValue;
  }

  uint32_t getLuxValue() const {
    return luxValue;
  }

  bool isTSLFound() const {
    return tslFound;
  }

   float getTemperatureValue() const {
    return temperatureValue;
  }

  float getHumidityValue() const {
    return humidityValue;
  }
  
};

Data data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  data.setupTSL();
  data.setupDHT();
}

void loop() {
  // put your main code here, to run repeatedly:
  data.readData();
  data.printData();



  // api call stuff here
//  uint16_t irValue = data.getIRValue();
//  uint16_t fullValue = data.getFullValue();
//  uint16_t visibleValue = data.getVisibleValue();
//  uint32_t luxValue = data.getLuxValue();
  delay(2000);

}