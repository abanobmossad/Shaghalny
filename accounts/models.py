import os
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.
COMPANY_DEFAULT_IMAGE = os.path.join(
    settings.STATIC_DIR, 'images', 'company.png')

USER_DEFAULT_IMAGE = os.path.join(
    settings.STATIC_DIR, 'images', 'user.png')


class User(AbstractUser):
    is_job_seeker = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)


class Company(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=140)
    description = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=140)
    industry = models.CharField(max_length=140)
    image = models.ImageField(upload_to="company_images",
                              default=COMPANY_DEFAULT_IMAGE, blank=True, null=True)

    def __str__(self):
        return self.company_name


class UserProfile(models.Model):

    CAREER_LIVEL_CHOICES = (
        ('ENTRY', 'Freshman'),
        ('EXPERIENCE_NM', 'Experienced (Non-Manager)'),
        ('MANAGER', 'Manager'),
    )
    JOB_TYPE_CHOICES = (
        ('FULL', 'Full Time'),
        ('PART', 'Part Time'),
        ('REMOTE', 'Remotely'),
    )
    LANGUAGES_CHOICES = (
        ('ARABIC', 'Arabic'),
        ('ENGLISH', 'English'),
        ('FRENCH', 'French'),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    career_levele = models.CharField(
        choices=CAREER_LIVEL_CHOICES,
        default='ENTRY',
        max_length=200
    )
    job_type = models.CharField(
        choices=JOB_TYPE_CHOICES,
        default='FULL',
        max_length=200
    )
    languages = models.CharField(
        choices=LANGUAGES_CHOICES,
        default='FULL',
        max_length=200
    )

    education = models.CharField(max_length=255)
    skills = models.CharField(max_length=300)
    salary = models.IntegerField()
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to="users_images",
                              default=USER_DEFAULT_IMAGE, blank=True, null=True)

    def __str__(self):
        return self.user.username
