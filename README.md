Cloud-Based Network Intrusion Detection System (NIDS)

A cloud-based Network Intrusion Detection System using Machine Learning,
deployed on AWS EC2 with real-time monitoring and alerting.

🚀 Features
- Isolation Forest anomaly detection
- Severity classification (High / Medium / Low)
- Flask-based dashboard
- Vertical bar chart & pie chart visualization
- AWS SNS email alerts
- Timestamped alerts (UTC)

 🏗 Architecture
- AWS EC2 (Ubuntu)
- Python, Scikit-learn, Pandas
- Flask
- HTML, CSS
- AWS SNS

 ▶ How to Run

```bash
python3 train_model.py
python3 detect.py
python3 app.py
