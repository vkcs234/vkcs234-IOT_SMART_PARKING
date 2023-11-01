from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
import json
class ParkingAvailabilityApp(App):
def build(self):
self.layout = BoxLayout(orientation='vertical')
self.availability_label = Label(text="Parking Availability: Loading...")
self.update_button = Button(text="Refresh Data")
self.update_button.bind(on_press=self.update_availability)
self.layout.add_widget(self.availability_label)
self.layout.add_widget(self.update_button)
return self.layout
def update_availability(self, instance):
url = "https://your-api-endpoint.com/parking-availability"
UrlRequest(url, self.parse_availability)
def parse_availability(self, request, result):
try:
data = json.loads(result)
available = data.get("available")
last_updated = data.get("lastUpdated")
self.availability_label.text = f"Parking Availability: {available} spots available\nLast updated: {last_updated}"
except Exception as e:
self.availability_label.text = "Failed to fetch data"
if __name__ == '__main__':
ParkingAvailabilityApp().run()
