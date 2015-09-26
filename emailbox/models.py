from django.db import models
# Create your models here.

class Email(models.Model):
    subject = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    sender = models.CharField(max_length=200)
    content = models.CharField(max_length=20000)
    important = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.subject
