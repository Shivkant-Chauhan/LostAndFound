from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title}"

class item(models.Model):
    person_first_name = models.CharField(max_length=100)
    person_last_name = models.CharField(max_length=100)

    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    roll_number = models.CharField(max_length=8, validators=[MinLengthValidator(8)])
    room_number = models.CharField(max_length=8, validators=[MinLengthValidator(8)])

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    #lost_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lost")
    #found_by = models.ForeignKey(User,blank=True, null=True, on_delete=models.CASCADE, related_name="found")

    def __str__(self):
        return f"{self.title}"
