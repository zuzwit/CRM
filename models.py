from django.db import models

# Create your models here.

class Users(models.Model):
    DELETED_CHOICES = (
        ('T','True'),
        ('F','False'),
    )

    ROLE_CHOICES = (
        ('1', 'Admin'),
        ('2', 'Moderator'),
        ('3', 'User'),
    )

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    dateOfBirth = models.DateField()
    login = models.CharField(unique=True,max_length=30)
    password = models.CharField(unique=True,max_length=30)
    role_id = models.CharField(max_length=1, choices=ROLE_CHOICES, default='3')
    isDeleted = models.CharField(max_length=1, choices=DELETED_CHOICES, default='F')