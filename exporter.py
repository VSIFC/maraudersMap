import json
import csv

class Exporter:
    @staticmethod
    def export(devices, file_path):
        if file_path.endswith(".json"):
            with open(file_path, "w") as f:
                json.dump(devices, f, indent=4)
        elif file_path.endswith(".csv"):
            with open(file_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "ip", "mac", "distance"])
                writer.writeheader()
                writer.writerows(devices)
        else:
            raise ValueError("Unsupported file format. Use .json or .csv.")
