from django.db import models

# Create your models here.
class Phonenumber(models.Model):
    name=models.CharField(max_length=100)
    is_spam=models.BooleanField(default=False)
    phone_no=models.CharField(max_length=20)

    def __str__(self):
        return self.phone_no
    

class User(models.Model):
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)


