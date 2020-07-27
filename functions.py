rf = 0
ws = 0
ntpset = 0
bright = 0

# toggle function
def toggle(p):
        p.value(not p.value())



# get battery voltage function

# formula is:
# ADC.read()/4096 * maximum voltage * ( resistor calculated / resistor actual)
# resistor calculated is from https://ohmslawcalculator.com/voltage-divider-calculator
# resistor actual is actual resistance used. Usually from preferred values.

def getBatteryVoltage(batteryvoltage):
	from machine import Pin, ADC

#ESP 8266
#	adc = machine.ADC(0)
#ESP 32
	adc = ADC(Pin(36))
	raw = adc.read()
#ESP 8266
#	return raw/1024 * batteryvoltage
#ESP 32
	return raw/4096 * batteryvoltage
#	return raw

# isr for rainfall counter
# rainfall interrupt callback
def rainfall_cb(d):
	global rf
	rf += 1
#	print("Rainfall toggled", rf)

# isr for wind speed counter
# rainfall interrupt callback
def windspeed_cb(d):
	global ws
	ws += 1
#	print("Windspeed toggled", ws)


# read the current wind direction  (just a place marker at the moment)
def getWinddir():
	from machine import Pin, ADC

	winddir = 0

#ESP 8266
#	adc = machine.ADC(0)
#ESP 32
	adc = ADC(Pin(35))
	raw = adc.read()
#ESP 8266
#	return raw/1024
#ESP 32
#	return raw/4096
	return raw

#	return winddir

# check if rtc needs updating from ntp after 30 minutes (1800 seconds)
def resetntp(t):
	global ntpset
	if (t > ntpset + 1800):
		ntpset = t
		return True
	return False
