from app.collectors.log_collector import LogCollector
from app.parser.linux_parser import LinuxLogParser
from app.detection.detector import DetectionEngine
from app.database.database import Database


def main():

    collector = LogCollector()
    parser = LinuxLogParser()
    detector = DetectionEngine()
    database = Database()

    logs = collector.read_log("samples/linux_auth.log")

    print("=" * 60)
    print("SOC Log Analyzer")
    print("=" * 60)

    for log in logs:

        event = parser.parse(log)

        if not event:
            continue

        print(event)

        database.insert_event(event)

        alerts = detector.analyze(event)

        for alert in alerts:

            print("\n🚨 SECURITY ALERT")
            print(alert)

            database.insert_alert(alert)

    database.show_events()
    database.show_alerts()

    database.close()


if __name__ == "__main__":
    main()