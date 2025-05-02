import requests
import time

class StarlinkTelemetryClient:
    BASE_URL = "https://api.starlink.com/telemetry/v1"

    def __init__(self, api_key=None):
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def get_satellite_telemetry(self, satellite_id):
        url = f"{self.BASE_URL}/satellites/{satellite_id}/telemetry"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_all_active_satellites(self):
        url = f"{self.BASE_URL}/satellites/active"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def stream_telemetry(self, satellite_id, interval=5):
        while True:
            try:
                telemetry = self.get_satellite_telemetry(satellite_id)
                yield telemetry
                time.sleep(interval)
            except Exception as e:
                print(f"Error fetching telemetry: {e}")
                time.sleep(interval)

if __name__ == "__main__":
    client = StarlinkTelemetryClient()
    active_sats = client.get_all_active_satellites()
    print(f"Active satellites count: {len(active_sats)}")
    if active_sats:
        sat_id = active_sats[0]['id']
        print(f"Streaming telemetry for satellite ID: {sat_id}")
        for data in client.stream_telemetry(sat_id, interval=10):
            print(data)
