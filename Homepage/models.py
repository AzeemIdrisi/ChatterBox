from django.db import models


class User(models.Model):
    uid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.uid


class Message(models.Model):
    text = models.TextField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.author.uid + " : " + self.text


class Reply(models.Model):
    text = models.TextField(max_length=500)
    original_message = models.ForeignKey(Message, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    is_author = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.author.uid + " : " + self.text
