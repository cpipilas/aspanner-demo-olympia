import time
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("OlympiaTestboardEthernet")


BATTERY_RELAY_PIN = "D2"
MAINS_RELAY_PIN = "D6"



# def test_measure_power_consumption():
#     print("")
#
#     INA219 = SpannerTestboard.INA219
#     time.sleep(1)
#
#     testboard.digitalWrite(BATTERY_RELAY_PIN, 'HIGH')
#     time.sleep(1)
#     print("Bus Voltage:")
#     print(testboard.ina219_getValue(INA219.BUS_VOLTAGE_V))
#     time.sleep(1)
#     print("Shunt Voltage:")
#     print(testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV))
#     time.sleep(1)
#     print("Current consumption (mA):")
#     print(testboard.ina219_getValue(INA219.CURRENT_MA))
#     testboard.digitalWrite(BATTERY_RELAY_PIN, 'LOW')
#     time.sleep(1)
#     print("Bus Voltage:")
#     print(testboard.ina219_getValue(INA219.BUS_VOLTAGE_V))
#     time.sleep(1)
#     print("Shunt Voltage:")
#     print(testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV))
#     time.sleep(1)
#     print("Current consumption (mA):")
#     print(testboard.ina219_getValue(INA219.CURRENT_MA))
#
#     testboard.digitalWrite(MAINS_RELAY_PIN, 'HIGH')
#     time.sleep(1)
#     testboard.digitalWrite(MAINS_RELAY_PIN, 'LOW')
#     time.sleep(1)
#
#     assert True == True



def test_measure_power_consumption():
    print("")
    testboard.digitalWrite(MAINS_RELAY_PIN, 'HIGH')
    testboard.digitalWrite(BATTERY_RELAY_PIN, 'HIGH')
    time.sleep(1)

    INA219 = SpannerTestboard.INA219
    time.sleep(1)


    print("Bus Voltage:")
    print(testboard.ina219_getValue(INA219.BUS_VOLTAGE_V))
    time.sleep(1)
    print("Shunt Voltage:")
    print(testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV))
    time.sleep(1)
    print("Current consumption (mA):")
    print(testboard.ina219_getValue(INA219.CURRENT_MA))
    time.sleep(1)


    testboard.digitalWrite(MAINS_RELAY_PIN, 'LOW')

    print("Bus Voltage:")
    print(testboard.ina219_getValue(INA219.BUS_VOLTAGE_V))
    time.sleep(1)
    print("Shunt Voltage:")
    print(testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV))
    time.sleep(1)
    print("Current consumption (mA):")
    print(testboard.ina219_getValue(INA219.CURRENT_MA))

    testboard.digitalWrite(MAINS_RELAY_PIN, 'HIGH')
    time.sleep(1)

    assert True == True
