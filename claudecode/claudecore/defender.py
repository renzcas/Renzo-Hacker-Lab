THRESHOLD = 12.0

def defend(anomaly):
    if anomaly["score"] > THRESHOLD:
        print(f"[DEFENSE] {anomaly['path']} blocked (score={anomaly['score']})")
