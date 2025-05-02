import hashlib
from datetime import datetime
import json

class KnownDeviceAdapter:
    def transform(self, raw_data):
        # Transform known device data format
        return raw_data

class GenericSensorAdapter:
    def transform(self, raw_data):
        # Transform generic sensor data format
        return raw_data

class UnknownDeviceHandler:
    def transform(self, raw_data):
        # Handle unknown device telemetry
        return raw_data

class MetadataSanitizer:
    def sanitize(self, data):
        # Remove sensitive metadata fields
        sanitized = data.copy()
        for key in ['mac', 'ssid', 'personal_info']:
            sanitized.pop(key, None)
        # Anonymize device id
        if 'device_mac' in data:
            mac = data['device_mac']
            sanitized['device_id'] = hashlib.sha3_256(mac.encode()).hexdigest()
        # Add timestamp
        sanitized['timestamp'] = datetime.utcnow().isoformat()
        return sanitized

class TimeSeriesDataLake:
    def __init__(self):
        self.storage = []

    def store(self, data):
        # Store data in time series format
        self.storage.append(data)

class UniversalSensorAggregator:
    def __init__(self):
        self.adapters = {
            'known': KnownDeviceAdapter(),
            'generic': GenericSensorAdapter(),
            'unknown': UnknownDeviceHandler()
        }
        self.metadata_processor = MetadataSanitizer()
        self.data_lake = TimeSeriesDataLake()

    def _detect_device_type(self, raw_data):
        # Simple heuristic for device type detection
        if 'device_mac' in raw_data:
            return 'known'
        elif 'sensor_type' in raw_data:
            return 'generic'
        else:
            return 'unknown'

    def ingest(self, raw_data):
        device_type = self._detect_device_type(raw_data)
        processed = self.adapters[device_type].transform(raw_data)
        anonymized = self.metadata_processor.sanitize(processed)
        self.data_lake.store(anonymized)

# Example usage
if __name__ == "__main__":
    aggregator = UniversalSensorAggregator()
    sample_data = {
        'device_mac': '00:11:22:33:44:55',
        'temperature': 22.5,
        'humidity': 45,
        'personal_info': 'user123'
    }
    aggregator.ingest(sample_data)
    print(json.dumps(aggregator.data_lake.storage, indent=2))
