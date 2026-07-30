from datetime import datetime


class Logger:

    def __init__(self):

        self.logs = []

    def log(self, level, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        entry = f"[{timestamp}] [{level}] {message}"

        self.logs.append(entry)

        print(entry)

    def info(self, message):

        self.log("INFO", message)

    def warning(self, message):

        self.log("WARNING", message)

    def error(self, message):

        self.log("ERROR", message)

    def get_logs(self):

        return self.logs

    def clear_logs(self):

        self.logs.clear()

        print("✅ Logs Cleared")


logger = Logger()