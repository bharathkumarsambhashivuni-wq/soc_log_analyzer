from collections import defaultdict


class DetectionEngine:
    """
    Detects suspicious activities from normalized events.
    """

    def __init__(self):
        self.failed_logins = defaultdict(int)

    def analyze(self, event):
        alerts = []

        if event["event_type"] == "failed_login":
            ip = event["source_ip"]

            self.failed_logins[ip] += 1

            if self.failed_logins[ip] >= 3:
                alerts.append({
                    "alert": "Possible Brute Force Attack",
                    "ip": ip,
                    "severity": "high",
                    "failed_attempts": self.failed_logins[ip]
                })

        return alerts