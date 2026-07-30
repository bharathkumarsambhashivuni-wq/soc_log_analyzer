from app.collectors.log_collector import LogCollector


def main():
    collector = LogCollector()

    logs = collector.read_log("samples/linux_auth.log")

    print("=" * 50)
    print("SOC Log Analyzer")
    print("=" * 50)

    for log in logs:
        print(log)


if __name__ == "__main__":
    main()