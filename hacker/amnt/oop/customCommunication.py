class CommunicationError(Exception):
    """Base class for communication-related exceptions."""
    pass

class ConnectionTimeoutError(CommunicationError):
    """Raised when a communication timeout occurs."""
    pass

class InvalidMessageError(CommunicationError):
    """Raised when a message format is invalid."""
    pass

class CommunicationHandler:
    def __init__(self):
        self.connected = False

    def connect(self):
        # Example: simulate connection logic
        print("Connecting...")
        self.connected = True

    def send_message(self, message):
        if not self.connected:
            raise CommunicationError("Not connected to server.")

        if not isinstance(message, str):
            raise InvalidMessageError("Message must be a string.")

        if len(message) == 0:
            raise InvalidMessageError("Message cannot be empty.")

        # Simulate sending logic (with a potential timeout)
        if "timeout" in message:
            raise ConnectionTimeoutError("Connection timed out while sending message.")

        print(f"Message sent: {message}")

handler = CommunicationHandler()

try:
    handler.connect()
    handler.send_message("hello world")
    handler.send_message("timeout message")  # This will raise ConnectionTimeoutError
except ConnectionTimeoutError as e:
    print(f"Timeout error: {e}")
except InvalidMessageError as e:
    print(f"Invalid message: {e}")
except CommunicationError as e:
    print(f"General communication error: {e}")
