from router_api import RouterAPI
from utils import calculate_distance

class DeviceData:
    @staticmethod
    def get_devices(refresh=False):
        raw_devices = RouterAPI.fetch_connected_devices()
        devices = []
        for device in raw_devices:
            device["distance"] = calculate_distance(device["rssi"])
            devices.append(device)
        return devices
