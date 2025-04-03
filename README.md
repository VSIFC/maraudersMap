# Product Requirements Document: WiFi Network Device Scanner CLI

## Overview
A command-line interface (CLI) tool to list all active device names connected to a WiFi network. The tool aggregates data from multiple access points/routers within a premise (e.g., school) to provide a comprehensive list of connected devices.

## Features
1. **Device Discovery**: Detect all active devices connected to the WiFi network.
2. **Multi-Access Point Support**: Aggregate data from multiple routers/access points.
3. **Device Name Resolution**: Display human-readable device names (if available).
4. **Real-Time Updates**: Provide an option to refresh the device list in real-time.
5. **Export Option**: Allow exporting the device list to a file (e.g., JSON or CSV).
6. **Device Distance Estimation**: Calculate and display the approximate distance between each detected device and the access point.

## Functional Requirements
1. The CLI must connect to routers via their APIs or SNMP to retrieve connected device data.
2. The CLI must parse and aggregate data from multiple access points.
3. The CLI must handle authentication for accessing router data.
4. The CLI must display the following for each device:
    - Device name
    - IP address
    - MAC address
    - Approximate distance from the access point
5. The CLI must provide a `--refresh` flag to update the device list in real-time.
6. The CLI must provide an `--export` flag to save the device list to a file.

## Non-Functional Requirements
1. The CLI must be cross-platform (Linux, macOS, Windows).
2. The CLI must handle network errors gracefully.
3. The CLI must have a response time of under 5 seconds for listing devices.

## Example Usage
```bash
# List all active devices
wifi-scanner list

# Refresh the device list in real-time
wifi-scanner list --refresh

# Export the device list to a JSON file
wifi-scanner list --export devices.json

# Run the CLI tool as a background process and log output to a file
wifi-scanner list > scanner.log 2>&1 &

# Tail the logs of the background process
tail -f scanner.log
```

## Run Guide
1. **Install Python**: Ensure Python 3.7 or higher is installed on your system.
2. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/maraudersMap.git
   cd maraudersMap
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the CLI Tool**:
   ```bash
   python wifi_scanner.py list
   ```

5. **Run as a Background Process**:
   ```bash
   python wifi_scanner.py list > scanner.log 2>&1 &
   ```

6. **Optional Flags**:
   - Use `--refresh` for real-time updates.
   - Use `--export <filename>` to save the device list to a file.

7. **Tail Logs**:
   ```bash
   tail -f scanner.log
   ```

## Technical Considerations
1. Use Python for implementation due to its rich networking libraries.
2. Use libraries like `scapy` or `paramiko` for network communication.
3. Use signal strength (RSSI) data to estimate the distance between devices and access points.
4. Ensure compatibility with common router APIs (e.g., Ubiquiti, Cisco, Netgear).

## Future Enhancements
1. Add support for detecting device types (e.g., phone, laptop, IoT).
2. Add a web-based interface for non-technical users.
3. Provide historical logs of connected devices.