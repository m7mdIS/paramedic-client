# Paramedic Client

Raspberry Pi app that scans fingerprints via GPIO/UART, retrieves patient data from backend server.

## Hardware Setup

Connect the Adafruit fingerprint sensor to Raspberry Pi GPIO:

- **VCC** → 3.3V or 5V (pin 1 or 2)
- **GND** → Ground (pin 6 or 9)
- **TX** (sensor) → **RX** (Pi GPIO 15, pin 10)
- **RX** (sensor) → **TX** (Pi GPIO 14, pin 8)

## Software Setup

1. **Enable UART on Raspberry Pi:**
   ```bash
   sudo raspi-config
   # Navigate to: Interface Options → Serial Port
   # Disable serial console, enable serial interface
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure UART port** (if needed):
   - Edit `fingerprint.py` and change `UART_PORT`:
     - `/dev/serial0` for Raspberry Pi 3+ (recommended)
     - `/dev/ttyAMA0` for older Raspberry Pi models

## Usage

```bash
python main.py
```

Select option 1 to scan a fingerprint. The system will:
1. Capture fingerprint from sensor
2. Search for match in sensor database
3. Fetch patient data from backend server
4. Display patient information
