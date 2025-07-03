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
        except (ValueError, TypeError):
            return False

jsonSerializer = JsonSerializer()
serialized = jsonSerializer.serialize("test")
print(serialized)  # Output: "test"
my_dict = {"test":1}
serialized = jsonSerializer.serialize(my_dict)
print(serialized)
print(isinstance(serialized, str))  # Output: True
print(jsonSerializer.is_valid_json(serialized))