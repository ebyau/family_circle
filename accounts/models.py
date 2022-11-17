from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime

from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from cloudinary_storage.validators import validate_video

# Create your models here.

#
# class Customer(models.Model):
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     date_created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self) -> str:
#         return self.name

class Audio(models.Model):

    name = models.CharField(max_length=200,null=True)
    message = models.TextField()
    date_created = models.DateTimeField(default=timezone.now(), blank=False)
    # file = models.ImageField(upload_to='kin-keepers/', blank=True, null=True, storage=VideoMediaCloudinaryStorage(),
                              # validators=[validate_video])
    file = CloudinaryField(resource_type='video',null=True,folder='kin-keepers/')


    def __str__(self) -> str:
        return str(self.file)
