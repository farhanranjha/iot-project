import network
import urequests
import time
import machine
from random import randint

SSID = "Home"
PASSWORD = "m55afthq"
API_URL = "https://iot.internal.ripeseed.io/iot/"
DEVICE_TAG = "myesp"
SEND_INTERVAL = 5

led = machine.Pin(2, machine.Pin.OUT)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)


def connect_wifi(timeout=20):
    if wlan.isconnected():
        return True
    
    print("Connecting to Wi-Fi...")
    wlan.connect(SSID, PASSWORD)
    
    start = time.time()
    while not wlan.isconnected():
        if time.time() - start > timeout:
            print("Wi-Fi connection timeout")
            return False
        time.sleep(0.5)
    
    print("Wi-Fi connected")
    return True

def blink_led(success=True, blink_count=3):
    if success:
        # Blink LED 3 times quickly for success
        for _ in range(blink_count):
            led.on()
            time.sleep_ms(200)
            led.off()
            time.sleep_ms(200)
    else:
        # Keep the LED on for failure for 2
        led.on()
        time.sleep_ms(2000)

def send_data():
    try:
        timestamp = time.localtime()
        timestamp_str = "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}Z".format(
            timestamp[0], timestamp[1], timestamp[2],
            timestamp[3], timestamp[4], timestamp[5]
        )
        
        payload = {
            "device_tag": DEVICE_TAG,
            "random_number": randint(0, 100),
            "data": {
                "temperature": 25.5,
                "pressure": 1013.25
            },
            "timestamp": timestamp_str
        }
        
        response = urequests.post(
            API_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200 or response.status_code == 201:
            print("Data sent successfully")
            blink_led(success=True)
            response.close()
            return True
        else:
            print("Server error:", response.status_code)
            blink_led(success=False)
            response.close()
            
    except OSError as e:
        print("Network error:", e)
        blink_led(success=False)
    except Exception as e:
        print("Request failed:", e)
        blink_led(success=False)


def main():
    if not connect_wifi():
        time.sleep(5)
        machine.reset()
    
    while True:
        send_data()
        time.sleep(SEND_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped")
        wlan.disconnect()
        wlan.active(False)
