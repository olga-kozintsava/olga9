
from django.db import models
from django.contrib.postgres.fields import JSONField


class NameModel(models.Model):
    name = JSONField()