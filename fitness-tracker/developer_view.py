from flask import Flask, render_template
from lib.utils import get_consumer

app = Flask(__name__, template_folder='template')

# Kafka consumer
consumer = get_consumer('health_data')


@app.route('/')
def index():
    return "Welcome to the Health Tracking App!"


@app.route('/Sunita_Sharma/health_data', methods=['GET'])
def get_health_data():
    messages = []
    for message in consumer:
        messages.append(message.value)
        if len(messages) >= 10:
            break

    return render_template('data.html', data=messages)


if __name__ == '__main__':
    app.run(port=8085)