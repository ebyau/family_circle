from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    message = models.TextField()
    file = models.FileField(upload_to='audios/',null=True)
    date_created = models.DateTimeField(default=timezone.now(),blank=False)


    def __str__(self) -> str:
        return self.name + ' ' + localtime(self.date_created).strftime("%Y-%m-%d %H:%M")


    