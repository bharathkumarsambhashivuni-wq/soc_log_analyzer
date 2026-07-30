from pathlib import Path


class LogCollector:
    """Reads log files from disk."""

    def __init__(self):
        self.supported_extensions = {".log"}

    def read_log(self, file_path):
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"{file_path} not found.")

        if path.suffix.lower() not in self.supported_extensions:
            raise ValueError("Unsupported log file.")

        with path.open("r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]