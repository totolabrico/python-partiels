class Version:
    def __init__(self, values):
        self.values = values

    @classmethod
    def from_string(cls, value):
        parts = value.split(".")
        if len(parts) != 3:
            cls.error("format is not correct")
            return None
        try:
            numbers = [int(v) for v in parts]
        except ValueError:
            cls.error("all parts must be integers")
            return None
        if any(v < 0 for v in numbers):
            cls.error("all values must be non-negative")
            return None
        return cls(numbers)

    def isMoreRecent(self, other):
        if not isinstance(other, Version):
            raise TypeError("Expected a Version instance")
        return self.values > other.values

    @staticmethod
    def error(msg):
        print("Version error:", msg)
