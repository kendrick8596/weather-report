# 🌦️ OOP Weather Engine

A robust, object-oriented Python application that interfaces with a professional weather API to provide real-time, validated weather data. This project demonstrates **clean code architecture**, **environment security**, and **defensive programming**.

## 🚀 Key Features
* **Hybrid OOP Architecture:** Separation of concerns between the `WeatherClient` (Service) and `WeatherReport` (Data Model).
* **Intelligent Location Mapping:** Prioritizes City/State queries to resolve global naming ambiguities (e.g., Alexandria, LA vs. Alexandria, Egypt).
* **Security First:** Utilizes `.env` files and `python-dotenv` to ensure API credentials never touch version control.
* **UX Focused CLI:** Custom `__str__` formatting with ANSI bolding for high-readability terminal output.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `requests`, `python-dotenv`
* **API:** [WeatherAPI.com](https://www.weatherapi.com/)

## 📂 Project Structure
```text
weather-app/
├── .env                # Private API credentials (ignored by git)
├── .gitignore          # Rules for excluded files
├── README.md           # Project documentation
├── requirements.txt    # Dependency list
└── weather_script.py   # Main application logic# weather-report
