from django.db import models

# Create your models here.

class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    phone_number = models.CharField(max_length=15)  # Assuming phone numbers are in string format
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    

    def __str__(self):
        return self.full_name
    
# after creating your models, always run the statements to execute it
# python manage.py makemigrations your_app_name
# python manage.py migrate
