import requests

class SessionHandler:
    def __init__(self) -> None:
        self.user_id = 0
        self.image_id = 0
        self.user_name = ""
        self.connection_time = ""

        self.url = "http://sendmessage.live:8001"

    def connect(self):
        response = requests.get(self.url)
        print(response)
    
    def process(self):
        pass