import random

class RouterAPI:
    @staticmethod
    def fetch_connected_devices():
        # Simulate fetching data from routers
        return [
            {"name": "Device1", "ip": "192.168.1.2", "mac": "AA:BB:CC:DD:EE:FF", "rssi": -40},
            {"name": "Device2", "ip": "192.168.1.3", "mac": "FF:EE:DD:CC:BB:AA", "rssi": -60},
        ]
