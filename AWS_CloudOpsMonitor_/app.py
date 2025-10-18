from flask import Flask, jsonify, request
from database import init_db, get_metrics
from alerts import send_alert

app = Flask(__name__)
init_db()  # Initialize DB connection

@app.route('/')
def home():
    return jsonify({"message": "CloudOpsMonitor Backend Running"})

@app.route('/metrics', methods=['GET'])
def metrics():
    data = get_metrics()
    # Simple threshold alert example
    for server in data:
        if server['cpu'] > 80:
            send_alert(f"High CPU Alert on {server['name']}")
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
