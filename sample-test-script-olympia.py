import time
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("OlympiaTestboardEthernet")


OUTPUT_PIN_1 = "D2"
OUTPUT_PIN_2 = "D6"



def test_measure_power_consumption():
    
#     BUS_VOLTAGE_V
#     SHUNT_VOLTAGE_MV
#     CURRENT_MA
    INA219 = SpannerTestboard.INA219
    time.sleep(1)
    print(testboard.ina219_getValue(INA219.BUS_VOLTAGE_V))
    time.sleep(1)
    print(testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV))
    time.sleep(1)
    print(testboard.ina219_getValue(INA219.CURRENT_MA))

    testboard.digitalWrite(OUTPUT_PIN_1, 'HIGH')
    time.sleep(1)
    testboard.digitalWrite(OUTPUT_PIN_1, 'LOW')
    time.sleep(1)

    testboard.digitalWrite(OUTPUT_PIN_2, 'HIGH')
    time.sleep(1)
    testboard.digitalWrite(OUTPUT_PIN_2, 'LOW')
    time.sleep(1)    
    assert True == True
