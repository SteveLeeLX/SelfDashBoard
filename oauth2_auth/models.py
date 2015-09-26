from django.db import models
from Dashboard import settings
from account_auth.models import Account
from oauth2client.django_orm import Storage
from oauth2client import client
from oauth2client.django_orm import FlowField, CredentialsField


class FlowModel(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, primary_key=True)
    flow = FlowField()


class CredentialsModel(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, primary_key=True)
    credential = CredentialsField()



