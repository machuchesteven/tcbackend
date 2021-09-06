from django.db import models


# extend the django default image field
class ImageField(models.ImageField):
    def value_to_string(self, obj):
        return obj.image.url





# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    image = ImageField(upload_to="services_image", default="/services_image/default.jpg", null=True, blank=True)

    def __str__(self):
        return self.name
    
    