from django.db import models


class Team(models.Model):
    name = models.TextField()
    code = models.TextField(unique=True)


class Winner(models.Model):
    team = models.OneToOneField("win.Team", on_delete=models.CASCADE)
    ts = models.DateTimeField(auto_now=True)
