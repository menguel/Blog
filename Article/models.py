from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images') # Installation de pillow requise pour ImageField

    def __str__(self):
        return self.name 