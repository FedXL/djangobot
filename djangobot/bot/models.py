from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, null=False)
    login = models.CharField(max_length=50, null=False)
    psw = models.CharField(max_length=50, null=False)


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=50, null=False)


class TeleUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=64, null=True)
    second_name = models.CharField(max_length=64, null=True)
    user_name = models.CharField(max_length=32, null=True)
    telegram_user_id = models.IntegerField(null=False)
    code = models.IntegerField(null=False)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    MESSAGE_TYPE_CHOICES = [
        ('Text', 'Text'),
        ('Document', 'Document'),
        ('File', 'File'),
    ]
    type = models.CharField(max_length=20, choices=MESSAGE_TYPE_CHOICES)
    text = models.TextField(max_length=4000)


