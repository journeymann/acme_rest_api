# accounts/models.py
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    date = models.CharField(max_length=15)
    account_num = models.IntegerField(help_text="(Account number)")
