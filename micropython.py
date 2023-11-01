import machine import time import urequests
sensor_pins = [(0, 1), (2, 3), (4, 5)] 
BEECEPTOR_ENDPOINT = "https://cloudplatform.free.beeceptor.com"
def measure_distance(trigger_pin, echo_pin):
	trigger = machine.Pin(trigger_pin, machine.Pin.OUT) 
	echo = machine.Pin(echo_pin, machine.Pin.IN)
	trigger = machine.Pin(trigger_pin, machine.Pin.OUT) 
	echo = machine.Pin(echo_pin, machine.Pin.IN)
	trigger.low()
	time.sleep_us(2) 
	trigger.high() 
	time.sleep_us(10) 
	trigger.low()
	while echo.value() == 0:
		signaloff = time.ticks_us()
	while echo.value() == 1: 
		signalon = time.ticks_us()
	timepassed = signalon - signaloff 
	distance = (timepassed * 0.0343) / 2 
return distance
def send_data_to_beeceptor(data):
	headers = {'Content-Type': 'application/json'} 
	json_data = {'occupancy': data} try: 
	response = urequests.post(BEECEPTOR_ENDPOINT, json=json_data, headers=headers)
	print("Data sent successfully")
	print(response.text) 
	print("An error occurred while sending data:", e)
while True:
sensor_data = [] 
distance = measure_distance(trigger_pin, echo_pin) 
print(f"Distance: {distance} cm from Sensor {sensor_pins.index((trigger_pin, echo_pin)) + 1}") 
occupancy = 1 if distance < 10 else 0 sensor_data.append(occupancy) send_data_to_beeceptor(sensor_data) 
time.sleep(5)
