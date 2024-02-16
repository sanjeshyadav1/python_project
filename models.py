from django.db import models
class Contact(models.Model):
   name = models.CharField(max_length=100)
   phone = models.CharField(max_length=20)
   user_pic = models.ImageField(max_length=200,null=True)

