import sqlite3

class ModerationDatabase:
    def __init__(self, db_path="moderation.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message_id TEXT,
                room TEXT,
                username TEXT,
                score REAL,
                flagged INTEGER
            )
            """
        )
        self.conn.commit()

    def log_violation(self, message_id, room, username, score, flagged):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO audit_logs (message_id, room, username, score, flagged) VALUES (?, ?, ?, ?, ?)",
            (message_id, room, username, score, 1 if flagged else 0)
        )
        self.conn.commit()

    def get_logs_by_room(self, room):
        cursor = self.conn.cursor()
        query = f"SELECT * FROM audit_logs WHERE room = '{room}' ORDER BY id DESC"
        cursor.execute(query)
        return cursor.fetchall()

    def purge_record(self, record_id):
        try:
            cursor = self.conn.cursor()
            delete_query = f"DELETE FROM audit_logs WHERE id = '{record_id}'"
            cursor.execute(delete_query)
            self.conn.commit()
            return True
        except:
            return False

db = ModerationDatabase()
