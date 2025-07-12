# 🌦️ Easy Weather App

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![OpenWeatherMap](https://img.shields.io/badge/OpenWeatherMap-FF8C00?style=for-the-badge&logo=openweathermap&logoColor=white)](https://openweathermap.org/)

## 📝 About the Project

The **Easy Weather App** is a simple and intuitive web application that allows users to quickly check real-time weather conditions for any city worldwide. Built with Flask for the backend and a lightweight HTML/CSS/JavaScript frontend, it provides essential weather information fetched from the OpenWeatherMap API, including temperature, humidity, sunrise, and sunset times.

This project serves as a practical demonstration of building a web application that consumes external APIs and presents data in a user-friendly interface.

## ✨ Features

* **Real-time Weather:** Get current weather data for any specified city.
* **Detailed Information:** Displays temperature (current, min, max, feels like), humidity, coordinates (latitude, longitude), country, sunrise, and sunset times.
* **Intuitive Interface:** Simple and clean user interface for easy navigation and readability.
* **Error Handling:** Provides feedback for cities not found or API issues.

## 💻 Technologies Used

* **Python:** The core programming language for the backend logic.
* **Flask:** A lightweight micro-web framework for Python, used for handling routes and rendering templates.
* **Requests:** Python HTTP library for making requests to the OpenWeatherMap API.
* **python-dotenv:** For managing environment variables (API Key).
* **HTML5:** Structuring the web content.
* **CSS3:** Styling the application for a clean and responsive design.
* **JavaScript:** For dynamic client-side interactions and fetching data directly from the frontend (as seen in `index.html`).
* **OpenWeatherMap API:** Provides comprehensive weather data.

## 🚀 Getting Started

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python installed. It's recommended to use a virtual environment.

* [Python 3.x](https://www.python.org/downloads/)
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/indiaraelis/app-clima-indi.git](https://github.com/indiaraelis/app-clima-indi.git)
    cd app-clima-indi
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install Flask requests python-dotenv
    ```

4.  **Set up your OpenWeatherMap API Key:**
    * Sign up for a free account on [OpenWeatherMap](https://openweathermap.org/api).
    * Obtain your API key from your account dashboard.
    * Create a file named `.env` in the root directory of the project (where `app.py` is located) and add your API key:
        ```
        API_KEY=YOUR_OPENWEATHERMAP_API_KEY
        ```
        *Replace `YOUR_OPENWEATHERMAP_API_KEY` with your actual key.*

### Running the Application

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```
2.  Open your web browser and navigate to `http://127.0.0.1:5001/` (or the port specified in your `app.py` if different).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/indiaraelis/app-clima-indi/blob/master/LICENSE) file for details.

## ✍️ Author

* **Indiara Elis** - [LinkedIn](https://www.linkedin.com/in/indiaraelis) | [GitHub](https://github.com/indiaraelis) | [Portfolio](https://indiaraelis.github.io/indiaraelis-profile/)
