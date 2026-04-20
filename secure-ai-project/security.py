import re
from datetime import datetime

def detect_prompt_injection(text):
    patterns = ["ignore", "override", "bypass", "hack", "system"]
    return any(word in text.lower() for word in patterns)

def detect_anomaly(text):
    if len(text) > 150:
        return True
    if re.search(r"(.)\1{4,}", text):
        return True
    if text.count("!") > 5:
        return True
    return False

def log_event(text, status):
    with open("logs.txt", "a") as f:
        f.write(f"{datetime.now()} | {status} | {text}\n")

def security_check(text):
    if detect_prompt_injection(text):
        log_event(text, "PROMPT_ATTACK")
        return False, "Prompt Injection Detected"

    if detect_anomaly(text):
        log_event(text, "ANOMALY_DETECTED")
        return False, "Anomalous Input Detected"

    log_event(text, "SAFE")
    return True, "Safe"