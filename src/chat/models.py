from django.contrib.auth import get_user_model
from django.db import models

user = get_user_model()


class Message(models.Model):
    author = models.ForeignKey(
        user, related_name="author_messages", on_delete=models.CASCADE
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    @staticmethod
    def last_messages(limit=20):
        return Message.objects.order_by("-timestamp").all()[:limit]
