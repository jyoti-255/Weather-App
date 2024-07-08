
## 🌤️  Weather App

📋 Introduction
The Weather App is a web application built using the Django framework that allows users to enter the name of a city and retrieve real-time weather information for that city. The application fetches data from the OpenWeatherMap API.

✨ Features
- 🌐 Search for real-time weather information by city name.
- 🌡️ Display temperature, weather conditions, humidity, wind speed, and more.
- 🖥️ User-friendly interface for entering city names and viewing weather data.

🛠️ Prerequisites
- 🐍 Python 3.x
- 🌐 Django 3.x or later
- 🔑 OpenWeatherMap API key

⚙️ Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the Django project:**
    ```bash
    cd weatherapp  
    python manage.py migrate
    python manage.py createsuperuser  
    ```

5. **Set up your OpenWeatherMap API key:**
    - Rename `.env.example` to `.env`.
    - Add your OpenWeatherMap API key in the `.env` file:
        ```plaintext
        WEATHER_API_KEY=your_api_key_here
        ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Open your web browser and navigate to:**
    ```plaintext
    http://127.0.0.1:8000
    ```

📝 Usage
1. **Enter the city name in the search box.**
2. **Submit the form to fetch and display the current weather information for the entered city.**

📁 Project Structure
```plaintext
weatherapp/
│
├── weatherapp/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── weather/
│   ├── templates/
│   │   └── weather/
│   │       └── home.html
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   └── ...
│
├── manage.py
├── requirements.txt
└── .env.example
