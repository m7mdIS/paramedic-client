import time
import serial
import adafruit_fingerprint

# Raspberry Pi GPIO UART (hardware UART on /dev/serial0 or /dev/ttyAMA0)
# Use /dev/serial0 for Raspberry Pi 3+ or /dev/ttyAMA0 for older models
UART_PORT = "/dev/serial0"  # Change to /dev/ttyAMA0 if needed
BAUDRATE = 57600


def scan_fingerprint():
    """Scan finger and search for an existing template on the sensor using Adafruit library.

    Returns the position number (template ID) if found; otherwise None.
    """
    try:
        # Initialize UART serial connection for GPIO
        uart = serial.Serial(UART_PORT, baudrate=BAUDRATE, timeout=1)
        
        # Initialize Adafruit fingerprint sensor
        sensor = adafruit_fingerprint.Adafruit_Fingerprint(uart)

        print("✔ Sensor initialized")
        print("Place your finger on the sensor...")

        # Wait for finger to be placed and capture image
        while sensor.get_image() != adafruit_fingerprint.OK:
            pass
        
        print("Image captured, processing...")

        # Convert image to template (buffer 1)
        if sensor.image_2_tz(1) != adafruit_fingerprint.OK:
            print("❌ Failed to convert image to template")
            return None

        # Search for matching fingerprint in sensor database
        if sensor.finger_search() != adafruit_fingerprint.OK:
            print("❌ No match found on the sensor")
            return None

        # Get the matched fingerprint ID
        fingerprint_id = sensor.finger_id
        confidence = sensor.confidence
        
        print(f"✅ Fingerprint match found (ID: {fingerprint_id}, Confidence: {confidence})")
        return fingerprint_id

    except serial.SerialException as exc:
        print(f"❌ Serial/UART error: {exc}")
        print(f"   Make sure UART is enabled on Raspberry Pi and sensor is connected to GPIO")
        return None
    except Exception as exc:
        print(f"❌ Fingerprint error: {exc}")
        return None

