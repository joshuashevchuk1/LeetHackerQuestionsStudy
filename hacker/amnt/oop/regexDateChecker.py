import re

class DateValidator:
    def __init__(self):
        self.pattern = re.compile(r"^(?:(?:[0-9]{4})-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])))$")

    def is_valid(self, date_str: str) -> bool:
        return bool(self.pattern.match(date_str))

# Example usage:
validator = DateValidator()
print(validator.is_valid("2023-12-25"))  # True
print(validator.is_valid("2023-02-30"))  # True (valid format, but not a real date)
print(validator.is_valid("23-12-25"))    # False

