from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

class Profile(models.Model):
    """
    db model to store the profile details of a user. 
    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('OTH', 'Others')
    )

    BLOOD_GROUP_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$')

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP_CHOICES, null=True)
    dob = models.DateField(null=True)
    contact_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    secondary_contact = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    joined = models.DateField(auto_now_add=True)
