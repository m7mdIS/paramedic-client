import serial
import adafruit_fingerprint

UART_PORT = "/dev/ttyS0"   # or /dev/serial0
BAUDRATE = 57600


def scan_fingerprint():
    try:
        uart = serial.Serial(UART_PORT, baudrate=BAUDRATE, timeout=1)
        finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

        print("✔ Sensor initialized")
        print("Place your finger on the sensor...")

        while finger.get_image() != adafruit_fingerprint.OK:
            pass

        if finger.image_2_tz(1) != adafruit_fingerprint.OK:
            return None

        if finger.finger_fast_search() != adafruit_fingerprint.OK:
            return None

        print(
            f"✅ Fingerprint match found "
            f"(ID: {finger.finger_id}, Confidence: {finger.confidence})"
        )
        return finger.finger_id

    except Exception as exc:
        print("❌ Fingerprint error:", exc)
        return None
