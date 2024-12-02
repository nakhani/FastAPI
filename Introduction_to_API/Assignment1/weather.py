import sys
import requests
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QMessageBox
from PySide6.QtGui import QPixmap
from ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
        self.apply_dark_mode()

    def initUI(self):
        self.setWindowTitle('Weather Forecast 🌤')
        self.ui.search_bar.setPlaceholderText('Enter city name')
        self.ui.btn_search.clicked.connect(self.get_weather)

        self.weather_info = QLabel('', self)
        self.weather_sticker = QLabel('', self)
        self.weather_forecast1 = QLabel('', self)
        self.weather_forecast2 = QLabel('', self)
        self.weather_forecast3 = QLabel('', self)

        self.ui.layout_today.addWidget(self.weather_sticker)
        self.ui.layout_today.addWidget(self.weather_info)
        self.ui.layout_forcast.addWidget(self.weather_forecast1)
        self.ui.layout_forcast.addWidget(self.weather_forecast2)
        self.ui.layout_forcast.addWidget(self.weather_forecast3)

    def get_weather(self):
        city = self.ui.search_bar.text()
        if not city:
            QMessageBox.warning(self, 'Input Error', 'Please enter a city name.')
            return

        url = f'https://goweather.herokuapp.com/weather/{city}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            self.display_weather(weather_data)
            self.display_forecast(weather_data)
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, 'API Error', 'Failed to fetch weather data.')
            print(f'Error: {e}')

    def display_weather(self, data):
        if 'temperature' in data and 'wind' in data and 'description' in data:
            self.weather_info.setText(
                f"Temperature: {data['temperature']}\n"
                f"Wind: {data['wind']}\n"
                f"Description: {data['description']}"
            )

            description = data['description']
            sticker_path = self.get_sticker_path(description)
            pixmap = QPixmap(sticker_path)
            self.weather_sticker.setPixmap(pixmap)
        else:
            QMessageBox.critical(self, 'Data Error', 'Incomplete weather data received.')

    def display_forecast(self, data):
        if 'forecast' in data:
            forecast_data = data['forecast']
            if len(forecast_data) >= 1:
                self.weather_forecast1.setText(
                    f"Day 1\n"
                    f"Temperature: {forecast_data[0]['temperature']}\n"
                    f"Wind: {forecast_data[0]['wind']}\n"
                )
            if len(forecast_data) >= 2:
                self.weather_forecast2.setText(
                    f"Day 2\n"
                    f"Temperature: {forecast_data[1]['temperature']}\n"
                    f"Wind: {forecast_data[1]['wind']}\n"
                )
            if len(forecast_data) >= 3:
                self.weather_forecast3.setText(
                    f"Day 3\n"
                    f"Temperature: {forecast_data[2]['temperature']}\n"
                    f"Wind: {forecast_data[2]['wind']}\n"
                )
        else:
            QMessageBox.critical(self, 'Data Error', 'No forecast data received.')

    def get_sticker_path(self, description):
        stickers = {
            "Partly cloudy": "stickers/partly_cloudy.png",
            "Sunny": "stickers/sun.png",
            "Mostly cloudy": "stickers/mostly_cloudy.png",
            "Overcast": "stickers/overcast.png",
            "Clear": "stickers/clear.png",
            "Hazy": "stickers/Hazy.png",
            "Scattered clouds": "stickers/scatter_cloud.png",
            "Broken clouds": "stickers/Broken clouds.png",
            "Foggy": "stickers/Foggy.png",
            "Rainy": "stickers/rainny.png",
            "Showery": "stickers/showery.png",
            "Drizzly": "stickers/drizzly.png",
            "Thunderstorms": "stickers/Thunderstorms.png",
            "Snowy": "stickers/snow.png",
            "Flurries": "stickers/flurries.png",
            "Blizzard": "stickers/blizzard.png",
            "Humid": "stickers/humidity.png",
            "Dry": "stickers/dry.png",
            "Muggy": "stickers/muggy.png",
            "Breezy": "stickers/breezy.png",
            "Calm": "stickers/calm.png",
        }
        return stickers.get(description, "stickers/default.png")

    def apply_dark_mode(self):
        dark_stylesheet = """
            QMainWindow {
                background-color: #2b2b2b;
                color: #f0f0f0;
            }
            QLabel {
                color: #f0f0f0;
            }
            QPushButton {
                background-color: #3b3b3b;
                color: #f0f0f0;
                border: 1px solid #555;
                border-radius: 4px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #444;
            }
            QLineEdit {
                background-color: #3b3b3b;
                color: #f0f0f0;
                border: 1px solid #555;
                border-radius: 4px;
                padding: 5px;
            }
            QMessageBox {
                background-color: #2b2b2b;
                color: #f0f0f0;
            }
        """
        self.setStyleSheet(dark_stylesheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
