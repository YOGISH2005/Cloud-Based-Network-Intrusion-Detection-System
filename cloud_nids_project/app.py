from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def dashboard():
    try:
        df = pd.read_csv("logs/alerts.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["timestamp","alert_type","source_ip","severity"])

    alerts = df.tail(10).to_dict(orient="records")

    high = (df["severity"] == "High").sum()
    medium = (df["severity"] == "Medium").sum()
    low = (df["severity"] == "Low").sum()

    return render_template(
        "dashboard.html",
        total_alerts=len(df),
        anomalies=high,
        emails_sent=max(0, high-1),
        alerts=alerts,
        high=high,
        medium=medium,
        low=low
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
