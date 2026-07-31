from app.collectors.log_collector import LogCollector
from app.parser.linux_parser import LinuxLogParser


def main():
    collector = LogCollector()
    parser = LinuxLogParser()

    logs = collector.read_log("samples/linux_auth.log")

    print("=" * 60)
    print("SOC Log Analyzer")
    print("=" * 60)

    for log in logs:
        event = parser.parse(log)

        if event:
            print(event)


if __name__ == "__main__":
    main()