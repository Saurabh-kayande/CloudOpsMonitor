def format_metrics(metrics):
    return [{"server": m['name'], "cpu": m['cpu'], "memory": m['memory']} for m in metrics]
