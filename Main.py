import sys
import requests
from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QLineEdit , QPushButton , QVBoxLayout 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class WheatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enther city name: " , self)
        self.city_input = QLineEdit(self)
        self.get_weather_time_button = QPushButton("Get Weather and Time: " , self)
        self.time_label = QLabel(self)
        self.temperature_label = QLabel( self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.iniUI()


    def iniUI(self):


    
        self.setWindowTitle("Time and Weather")
        self.setWindowIcon(QIcon("Icon.png"))

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_time_button)
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_time_button.setObjectName("get_weather_time_button")
        self.time_label.setObjectName("time_label")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QWidget {
                background-color: #020617;
            }

            QLabel {
                color: white;
                font-family: Comic Sans MS;
            }

            QLineEdit#city_input {
                background-color: #222;
                color: white;
                border: 2px solid #444;
                border-radius: 10px;
                padding: 10px 14px;
                font-size: 36px;
            }

            QLineEdit#city_input:focus {
                border: 2px solid #00ffcc;
            }

            QPushButton#get_weather_time_button {
                background-color: #16a34a;
                color: white;
                border: none;
                border-radius: 22px;
                padding: 14px 14px;
                font-size: 32px;
                font-family: Arial;
                font-weight: bold;
                min-height: 40px;
                min-width: 340px;
            }

            QPushButton#get_weather_time_button:hover {
                background-color: #15803d;
            }

            QPushButton#get_weather_time_button:pressed {
                background-color: #166534;
            }

            QLabel#time_label {
                font-size: 90px;
                color: #a5f3fc;
                font-family: Arial;
                font-weight: bold;
                background: transparent;
            }

            QLabel#temperature_label {
                font-size: 110px;
                color: #7dd3fc;
                font-family: Arial;
                font-weight: bold;
                background: transparent;
            }

            QLabel#emoji_label {
                font-size: 140px;
                min-height: 160px;
                background: transparent;
                font-family: Segoe UI Emoji, sans-serif;
            }

            QLabel#description_label {
                font-size: 54px;
                color: #e5e7eb;
                font-style: italic;
                background: transparent;
            }

            QLabel#city_label {
                font-size: 44px;
                font-style: italic;
                color: #cbd5e1;
                background: transparent;
            }

            /* Error state override example */
            QLabel#temperature_label[error="true"] {
                font-size: 52px;
                color: #f87171;
            }
        """)

        self.get_weather_time_button.clicked.connect(self.get_weather)
    def get_weather(self):
        api_key = "Your Api key"
        city = self.city_input.text().strip()
        
        if not city:
            self.display_error("Please enter a city name")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get("cod") != 200:
                self.display_error("City not found")
                return

            self.display_weather(data)
            self.get_time(city)          

        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                self.display_error("City not found")
            else:
                self.display_error(f"HTTP error: {response.status_code}")
        except requests.exceptions.ConnectionError:
            self.display_error("No internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Request timed out")
        except Exception as e:
            self.display_error("Something went wrong")


    def get_time(self, city):
        url = "https://api.ipgeolocation.io/timezone"
        params = {
            "apiKey": "Your Api key",
            "city": city
        }

        try:
            res = requests.get(url, params=params, timeout=10)
            res.raise_for_status()
            data = res.json()

            if "message" in data or "error" in data:
                return

            self.display_time(data)

        except Exception:
            pass


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 40px;")
        self.temperature_label.setText(message)
        self.time_label.hide()               
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self , data):
        self.time_label.show()
        self.temperature_label.setStyleSheet("font-size: 75px;")
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]

        self.description_label.setText(weather_description)
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.temperature_label.setText(f"{data['main']['temp']:.0f}°C")
    

    def display_time (self , data):
        self.time_label.setStyleSheet("font-size: 75px;")
        time = data["time_24"][:5]
        self.time_label.setText(time)

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <=232:
            return"⚡"
        elif 300 <= weather_id <=321:
            return"⛅"
        elif 500 <= weather_id <=531:
            return"☔"
        elif 600 <= weather_id <=622:
            return"⛄"
        elif 701 <= weather_id <=741:
            return"🍃"
        elif weather_id == 762:
            return"🌋"
        elif weather_id == 771:
            return"💨"
        elif weather_id == 781:
            return"🌪"
        elif weather_id == 800:
            return"🌞"
        elif 801 <= weather_id <=804:
            return"☁"
        else:
            return""
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wheather_app = WheatherApp()
    wheather_app.show()
    sys.exit(app.exec_())
