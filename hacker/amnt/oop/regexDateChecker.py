import re
from datetime import datetime

class DateValidator:
    def __init__(self, raw_pattern: str = r"\d{4}-\d{2}-\d{2}"):
        escaped = re.escape(raw_pattern)
        self.pattern = re.compile(escaped)  # Would match literally: \d{4}-\d{2}-\d{2}
        self.regex_check = re.compile(raw_pattern)  # Proper actual regex

    def is_valid(self, date_str: str) -> bool:
        if not self.regex_check.match(date_str):
            return False
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

data_check = "2023-12-25"
validator = DateValidator()
print(validator.is_valid("2023-12-25"))


def data_checker(s):
    raw_pattern = r"\d{4}-\d{2}-\d{2}"
    pattern = re.compile(raw_pattern)
    if not pattern.match(s):
        return False
    try:
        datetime.strptime(s, "%Y-%m-%d")
        return True
    except ValueError:
        return False

print(data_checker("2023-12-25"))
