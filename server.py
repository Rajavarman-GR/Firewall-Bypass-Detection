from flask import Flask, render_template, request, jsonify
import pandas as pd
import os
import random
from datetime import datetime
from collections import defaultdict
from firewall_rules import block_ip, is_ip_blocked

import matplotlib
matplotlib.use('Agg')  # ← ✅ USE THIS BACKEND FOR HEADLESS / SERVER PLOTTING
import matplotlib.pyplot as plt

app = Flask(__name__)
THREATS_FILE = 'threats.xlsx'
ATTEMPT_LIMIT = 3
attack_counts = defaultdict(int)

def initialize_excel():
    if not os.path.exists(THREATS_FILE):
        df = pd.DataFrame(columns=["IP", "Country", "Threat Type", "Timestamp"])
        df.to_excel(THREATS_FILE, index=False, engine='openpyxl')

def log_threat(ip, country, threat_type):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame([[ip, country, threat_type, timestamp]],
                             columns=["IP", "Country", "Threat Type", "Timestamp"])
    df = pd.read_excel(THREATS_FILE, engine='openpyxl')
    updated_df = pd.concat([df, new_entry], ignore_index=True)
    updated_df.to_excel(THREATS_FILE, index=False, engine='openpyxl')
    attack_counts[ip] += 1
    if attack_counts[ip] >= ATTEMPT_LIMIT and not is_ip_blocked(ip):
        block_ip(ip)

def generate_graph():
    try:
        df = pd.read_excel(THREATS_FILE, engine='openpyxl')
        if "Country" in df.columns and not df.empty:
            country_counts = df["Country"].value_counts()
            plt.figure(figsize=(8, 4))
            country_counts.plot(kind="bar", color="purple")
            plt.title("Threats by Country")
            plt.xlabel("Country")
            plt.ylabel("Count")
            plt.tight_layout()
            graph_path = os.path.join("static", "logs", "threats_graph.png")
            os.makedirs(os.path.dirname(graph_path), exist_ok=True)
            plt.savefig(graph_path)
            plt.close()
    except Exception as e:
        print(f"Graph generation error: {e}")

@app.route("/")
def index():
    generate_graph()
    return render_template("index.html")

@app.route("/simulate_attack", methods=["POST"])
def simulate_attack():
    fake_ips = ["192.168.1.100", "10.0.0.50", "172.16.0.200"]
    countries = ["USA", "China", "Russia", "India", "Germany"]
    threats = ["SQL Injection", "DDoS", "Port Scan", "XSS", "Brute Force"]
    ip = random.choice(fake_ips)
    country = random.choice(countries)
    threat = random.choice(threats)
    log_threat(ip, country, threat)
    return jsonify({"message": f"Simulated attack from {ip} ({country}) using {threat}."})

@app.route("/get_logs")
def get_logs():
    try:
        df = pd.read_excel(THREATS_FILE, engine='openpyxl')
        return df.tail(10).to_json(orient="records")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/update_graph")
def update_graph():
    generate_graph()
    return jsonify({"status": "success"})

if __name__ == "__main__":
    initialize_excel()
    app.run(debug=True)
