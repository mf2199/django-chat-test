import json

from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Message

user = get_user_model()


class ChatConsumer(WebsocketConsumer):
    def __init__(self):
        super().__init__()
        self.room_name = None
        self.room_group_name = None

    def fetch_messages(self, data):
        messages = Message.last_messages()
        content = {
            "command": "messages",
            "messages": self.messages_to_json(messages),
        }
        self.send_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(
                {
                    "author": message.author.username,
                    "content": message.content,
                    "timestamp": str(message.timestamp),
                }
            )

        return result

    def new_message(self, data):
        author = data["from"]
        author_user = user.objects.filter(username=author)[0]
        message = Message.objects.create(
            author=author_user, content=data["message"]
        )
        content = {
            "command": "new_message",
            "message": {
                "author": message.author.username,
                "content": message.content,
                "timestamp": str(message.timestamp),
            }
        }

        return self.send_chat_message(content)

    commands = {
        "fetch_messages": fetch_messages,
        "new_message": new_message,
    }

    def connect(self):
        """Join the room group."""
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        """Leave room group."""
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        """Receives message from WebSocket and sends message to the room group.
        """
        data = json.loads(text_data)
        self.commands[data["command"]](self, data)

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        """Receives message from the room group and sends message to WebSocket.
        """
        message = event["message"]

        self.send(text_data=json.dumps(message))
