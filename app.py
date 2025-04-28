from flask import Flask, render_template, request, jsonify, redirect
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')

# Função para converter timestamp para hora legível
@app.template_filter('timestamp_to_time')
def timestamp_to_time(timestamp):
    if timestamp is None:
        return 'Indefinido'
    try:
        return datetime.utcfromtimestamp(timestamp).strftime('%H:%M:%S')
    except Exception as e:
        return f'Erro: {e}'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            return redirect(f'/weather/{city}')
    return render_template('index.html')

@app.route('/weather/<city>', methods=['GET'])
def weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt_br'
    response = requests.get(url)

    if response.status_code != 200:
        return render_template('index.html', error="Cidade não encontrada")

    weather_data = response.json()

    # Convertendo os timestamps de sunrise e sunset
    sunrise = weather_data['sys'].get('sunrise')
    sunset = weather_data['sys'].get('sunset')

    sunrise_time = timestamp_to_time(sunrise)
    sunset_time = timestamp_to_time(sunset)

    result = {
        'cidade': weather_data['name'],
        'pais': weather_data['sys']['country'],
        'latitude': weather_data['coord']['lat'],
        'longitude': weather_data['coord']['lon'],
        'temperatura': weather_data['main']['temp'],
        'temperatura_min': weather_data['main']['temp_min'],
        'temperatura_max': weather_data['main']['temp_max'],
        'sensacao_termica': weather_data['main']['feels_like'],
        'sunrise': sunrise_time,
        'sunset': sunset_time
    }

    return render_template('index.html', result=result)

# Definindo a porta a partir da variável de ambiente (para ambientes de deploy)
port = int(os.environ.get('PORT', 5001))  # 5001 é a porta padrão local para o Flask

if __name__ == "__main__":
    # Garantindo que o Flask escute em todas as interfaces de rede (0.0.0.0) e na porta certa
    app.run(host='0.0.0.0', port=port)
