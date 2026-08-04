import sqlite3
from pathlib import Path


class Database:

    def __init__(self):
        Path("data").mkdir(exist_ok=True)

        self.connection = sqlite3.connect("data/soc_logs.db")
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            hostname TEXT,
            service TEXT,
            username TEXT,
            source_ip TEXT,
            event_type TEXT,
            severity TEXT

        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            alert TEXT,
            ip TEXT,
            severity TEXT,
            failed_attempts INTEGER

        )
        """)

        self.connection.commit()

    def insert_event(self, event):

        self.cursor.execute("""
        INSERT INTO events
        (
        timestamp,
        hostname,
        service,
        username,
        source_ip,
        event_type,
        severity
        )
        VALUES (?,?,?,?,?,?,?)
        """,
        (
            event["timestamp"],
            event["hostname"],
            event["service"],
            event["username"],
            event["source_ip"],
            event["event_type"],
            event["severity"]
        ))

        self.connection.commit()

    def insert_alert(self, alert):

        self.cursor.execute("""
        INSERT INTO alerts
        (
        alert,
        ip,
        severity,
        failed_attempts
        )
        VALUES (?,?,?,?)
        """,
        (
            alert["alert"],
            alert["ip"],
            alert["severity"],
            alert["failed_attempts"]
        ))

        self.connection.commit()

    def show_events(self):

        rows = self.cursor.execute(
            "SELECT * FROM events"
        ).fetchall()

        print("\n========== EVENTS ==========")

        for row in rows:
            print(row)

    def show_alerts(self):

        rows = self.cursor.execute(
            "SELECT * FROM alerts"
        ).fetchall()

        print("\n========== ALERTS ==========")

        for row in rows:
            print(row)

    def close(self):
        self.connection.close()