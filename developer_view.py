from flask import Flask, render_template
from lib.utils import get_consumer

app = Flask(__name__, template_folder='template')

# Kafka consumer
consumer = get_consumer('health_data')

@app.route('/')
def index():
    """
    Renders the index page with a welcome message.

    Returns:
        str: A string containing the welcome message.
    """
    return "Welcome to the Health Tracking App!"

@app.route('/Sunita_Sharma/health_data', methods=['GET'])
def get_health_data():
    """
    Retrieves health data from the Kafka consumer and renders it in a template.

    Returns:
        flask.Response: The rendered template containing the health data.
    """
    messages = []
    for message in consumer:
        messages.append(message.value)
        if len(messages) >= 10:
            break

    return render_template('data.html', data=messages)

if __name__ == '__main__':
    """
    Runs the Flask application.

    It starts the server and listens on port 8085 for incoming requests.
    """
    app.run(port=8085)
