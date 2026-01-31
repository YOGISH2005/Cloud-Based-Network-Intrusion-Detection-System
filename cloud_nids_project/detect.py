import pandas as pd
import numpy as np
from datetime import datetime, timezone

alerts = []

for i in range(30):
    score = np.random.random()

    if score > 0.8:
        severity = "High"
    elif score > 0.5:
        severity = "Medium"
    else:
        severity = "Low"

    alerts.append({
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "alert_type": "Anomaly",
        "source_ip": "172.31.33.215",
        "severity": severity
    })

df = pd.DataFrame(alerts)
df.to_csv("logs/alerts.csv", index=False)

print("Alerts generated")
