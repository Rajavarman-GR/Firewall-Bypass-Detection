Firewall Bypass Detection System

A fully functional real-time Firewall Bypass Detection and Countermeasure System developed using Python, Flask, and Machine Learning. This project simulates attack detection, auto-blocks repeated threats, and visualizes threat logs using dynamic graphs — all in a sleek cyber-themed web dashboard.

------------------------

🚀 Features

✅ Real-Time Anomaly Detection
✅ Simulated Cyber Attacks (SQLi, DDoS, Port Scanning)
✅ Auto-Blocking of IPs after Threshold
✅ Threat Logging into Excel (threats.xlsx)
✅ Real-Time Threat Visualization (Graphs)
✅ Animated Gradient Cyber UI (HTML/CSS)
✅ Geolocation Tracking Support (optional)
✅ Email Alerts (optional integration)
✅ User Authentication (optional)

------------------------

📁 Folder Structure

Firewall_Bypass_Detection/
├── server.py                  # Flask backend with simulation & detection
├── firewall_rules.py          # IP auto-blocking logic
├── anomaly_model.pkl          # ML model (optional)
├── threats.xlsx               # Logged threats
├── requirements.txt           # Project dependencies
├── templates/
│   └── index.html             # Dashboard HTML
├── static/
│   ├── styles.css             # UI styling and animations
│   ├── firewall_anim.gif      # Cyber-style visual (animated)
│   └── logs/
│       └── threats_graph.png  # Auto-generated threat graph

------------------------

⚙️ Installation

1. Clone the Repository:
   git clone https://github.com/Rajavarman-GR/Firewall-Bypass-Detection-
   cd firewall-bypass-detection

2. Install Requirements:
   pip install -r requirements.txt

3. Run the Application:
   python server.py

4. Open in Browser:
   http://127.0.0.1:5000

------------------------

🧪 Simulate Attacks

Use the "Simulate Attack" button to test SQL Injection, DDoS, Port Scans, and more. Each attack is logged and plotted in real-time. After X attempts, IPs are auto-blocked by the firewall_rules.py module.

------------------------

📬 Optional Email Alerts

Set up email alerts in server.py using:
smtplib.SMTP_SSL("smtp.gmail.com", 465)
Configure with your credentials or use secure app passwords.

------------------------

🔐 Optional: Authentication

Protect your dashboard by enabling basic Flask login (see server.py snippet in docs).

------------------------

📈 Live Graphs & Logging

- Logs are auto-appended in threats.xlsx
- matplotlib generates a live threat bar chart (threats_graph.png)
- Visualizations auto-refresh in dashboard every 5 seconds

------------------------

💡 Future Enhancements

- GeoIP-based mapping (using APIs)
- Packet sniffing (Scapy integration)
- SMS/email alerting on high-risk anomalies
- Admin panel for managing blocked IPs
- Docker container support

------------------------

🧠 Authors

Rajavarman – Project Developer & UI Designer
LinkedIn: https://linkedin.com/in/rajavarman-g-r
GitHub: https://github.com/Rajavarman-GR

------------------------

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

------------------------

🤝 Contributions

Pull requests, suggestions, and forks are welcome. For major changes, please open an issue first to discuss what you'd like to change.

------------------------

📚 References

Flask Documentation - https://flask.palletsprojects.com/
Pandas Documentation - https://pandas.pydata.org/
Matplotlib Docs - https://matplotlib.org/
OpenPyXL - https://openpyxl.readthedocs.io/
scikit-learn - https://scikit-learn.org/
