import json

class JsonSerializer():
    def __init__(self):
        pass

    def serialize(self, obj):
        return json.dumps(obj)

    def is_valid_json(self,obj):
        try:
            json.loads(obj)
            return True
        except Exception:
            raise NoSpecialException()

class InValidJson(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return f"{self.args[0]}"

class MyCustomException(Exception):
    def __init__(self,message):
        super().__init__(message)

    def __str__(self):
        return f"{self.args[0]}"

class NoSpecialException(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "NoSpecialException yo yo yo yo"



jsonSerializer = JsonSerializer()
serialized = jsonSerializer.serialize("test")
print(serialized)  # Output: "test"
my_dict = {"test":1}
serialized = jsonSerializer.serialize(my_dict)
print(serialized)
print(isinstance(serialized, str))  # Output: True
print(jsonSerializer.is_valid_json(serialized))
notJson = 1234
print(jsonSerializer.is_valid_json(notJson))
