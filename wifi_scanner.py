import argparse
import json
import time
from typing import List, Dict
import requests  # For API calls
from pysnmp.hlapi import *  # For SNMP interactions

API_URL = "http://192.168.1.1/api/devices"  # Replace with your router's actual API endpoint

def fetch_connected_devices() -> List[Dict]:
    """
    Fetches connected devices from routers using API or SNMP.
    """
    devices = []

    # Fetch data from a router API
    try:
        response = requests.get(API_URL, auth=("admin", "password"))
        response.raise_for_status()
        api_devices = response.json()
        for device in api_devices:
            devices.append({
                "name": device.get("name", "Unknown"),
                "ip": device.get("ip", "Unknown"),
                "mac": device.get("mac", "Unknown"),
                "distance": device.get("distance", 0)  # Assume distance is provided
            })
    except requests.RequestException as e:
        print(f"Error fetching devices via API: {e}")

    # Fetch data using SNMP
    try:
        iterator = nextCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('192.168.1.1', 161)),
            ContextData(),
            ObjectType(ObjectIdentity('1.3.6.1.2.1.4.22.1.2')),  # Example OID for ARP table
            lexicographicMode=False
        )
        for errorIndication, errorStatus, errorIndex, varBinds in iterator:
            if errorIndication:
                print(f"SNMP error: {errorIndication}")
                break
            elif errorStatus:
                print(f"SNMP error at {errorIndex}: {errorStatus.prettyPrint()}")
                break
            else:
                for varBind in varBinds:
                    mac_address = str(varBind[1])
                    devices.append({
                        "name": "Unknown",  # SNMP may not provide device names
                        "ip": "Unknown",   # Replace with actual IP extraction logic
                        "mac": mac_address,
                        "distance": 0      # Distance calculation not available via SNMP
                    })
    except Exception as e:
        print(f"Error fetching devices via SNMP: {e}")

    return devices

def list_devices():
    """
    Lists all connected devices.
    """
    devices = fetch_connected_devices()
    print(f"{'Name':<20} {'IP Address':<15} {'MAC Address':<20} {'Distance (m)':<10}")
    print("-" * 65)
    for device in devices:
        print(f"{device['name']:<20} {device['ip']:<15} {device['mac']:<20} {device['distance']:<10}")

def export_devices(filename: str):
    """
    Exports the connected devices to a file.
    """
    devices = fetch_connected_devices()
    with open(filename, 'w') as file:
        json.dump(devices, file, indent=4)
    print(f"Device list exported to {filename}")

def real_time_updates():
    """
    Continuously refreshes and displays the device list in real-time.
    """
    try:
        while True:
            print("\nRefreshing device list...\n")
            list_devices()
            time.sleep(5)  # Refresh every 5 seconds
    except KeyboardInterrupt:
        print("\nReal-time updates stopped.")

def main():
    parser = argparse.ArgumentParser(description="WiFi Network Device Scanner CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Subcommand: list
    list_parser = subparsers.add_parser("list", help="List all active devices")
    list_parser.add_argument("--refresh", action="store_true", help="Refresh the device list in real-time")
    list_parser.add_argument("--export", type=str, help="Export the device list to a file (e.g., JSON)")

    args = parser.parse_args()

    if args.command == "list":
        if args.refresh:
            real_time_updates()
        elif args.export:
            export_devices(args.export)
        else:
            list_devices()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()