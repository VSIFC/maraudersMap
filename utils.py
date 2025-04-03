def calculate_distance(rssi):
    # Simplified formula for RSSI to distance conversion
    tx_power = -50  # Assumed transmit power in dBm
    return round(10 ** ((tx_power - rssi) / 20), 2)
