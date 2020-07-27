rf = 0
ws = 0
ntpset = 0

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
	global esp32

	if (esp32):
		#ESP 32
		adc = ADC(Pin(36))
		raw = adc.read()
		return raw/4096 * batteryvoltage

	else:
		#ESP 8266
		adc = machine.ADC(0)
		return raw/1024 * batteryvoltage


# isr for rainfall counter
# rainfall interrupt callback
def rainfall_cb(d):
	global rf
	rf += 1

# isr for wind speed counter
# rainfall interrupt callback
def windspeed_cb(d):
	global ws
	ws += 1


# read the current wind direction  (just a place marker at the moment)
"""
for esp32 can use reed swithed windvane and use an ADC pin to get direction reading.
for esp8266 would have to need a Holman type wind vane which outputs a direction number between 0 and 15 this requires further programming
"""

def getWinddir():
	from machine import Pin, ADC
	global esp32

	winddir = 0

	if (esp32):
		#ESP 32
		adc = ADC(Pin(35))
		raw = adc.read()
	else:
		#ESP 8266
		adc = machine.ADC(0)

#	return raw
	return winddir



# check if rtc needs updating from ntp after 30 minutes (1800 seconds)
def resetntp(t):
	global ntpset
	if (t > ntpset + 1800):
		ntpset = t
		return True
	return False

