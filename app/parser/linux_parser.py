import re


class LinuxLogParser:
    """Parses Linux SSH authentication logs."""

    pattern = re.compile(
        r"(?P<month>\w+)\s+"
        r"(?P<day>\d+)\s+"
        r"(?P<time>\d{2}:\d{2}:\d{2})\s+"
        r"(?P<hostname>\S+)\s+"
        r"(?P<service>\w+)\[\d+\]:\s+"
        r"(?P<status>Failed|Accepted)\s+password\s+for\s+"
        r"(?P<username>\S+)\s+from\s+"
        r"(?P<ip>\d+\.\d+\.\d+\.\d+)"
    )

    def parse(self, log_line):
        match = self.pattern.search(log_line)

        if not match:
            return None

        data = match.groupdict()

        event = {
            "timestamp": f"{data['month']} {data['day']} {data['time']}",
            "hostname": data["hostname"],
            "service": data["service"],
            "username": data["username"],
            "source_ip": data["ip"],
            "event_type": (
                "failed_login"
                if data["status"] == "Failed"
                else "successful_login"
            ),
            "severity": (
                "medium"
                if data["status"] == "Failed"
                else "info"
            ),
        }

        return event