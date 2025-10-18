# Placeholder for advanced metric processing
def process_metrics(metrics):
    alerts = []
    for server in metrics:
        if server['cpu'] > 80:
            alerts.append(f"High CPU on {server['name']}")
    return alerts
