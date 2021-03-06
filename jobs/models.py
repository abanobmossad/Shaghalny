import os
from django.db import models
from django.conf import settings
from django.urls import reverse
from accounts.models import Company,UserProfile
from django.utils import timezone, text

# Create your models here.
COMPANY_DEFAULT_IMAGE = os.path.join(
    settings.STATIC_DIR, 'images', 'company.png')


class Job(models.Model):

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
    slug = models.SlugField(max_length=400)
    title = models.CharField(max_length=140)
    company = models.ForeignKey(
        Company, on_delete=models.DO_NOTHING, related_name="jobs")
    description = models.TextField()
    requirements = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)
    career_levele = models.CharField(
        choices=CAREER_LIVEL_CHOICES,
        default='ENTRY',
        max_length=150,
    )
    job_type = models.CharField(
        choices=JOB_TYPE_CHOICES,
        default='FULL',
        max_length=150,

    )
    languages = models.CharField(
        choices=LANGUAGES_CHOICES,
        default='FULL',
        max_length=150,

    )
    experience_needed = models.IntegerField(default=1)
    open_vacancies = models.IntegerField(default=1)
    applications = models.ManyToManyField(
        UserProfile, related_name="application_users")
    saved_jobs = models.ManyToManyField(
        UserProfile, related_name="user_saved_jobs")

    def __str__(self):
        return text.slugify("{} --{} {} ---{}".format(self.title,
                                                      self.company, self.company.address, self.date))
