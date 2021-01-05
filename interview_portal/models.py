from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator


class Technology(models.Model):
    class Meta:
        verbose_name_plural = "technologies"

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Status(models.Model):
    class Meta:
        verbose_name_plural = "status"

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    TYPE_CHOICES = [('CL', 'Client'), ('CA', 'Candidate')]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='CA')
    technology = models.ForeignKey('Technology', on_delete=models.PROTECT)
    current_status = models.ForeignKey(Status, on_delete=models.PROTECT)
    applied_on = models.DateTimeField(auto_now_add=True)
    moved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ApplicationDetail(models.Model):
    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE,
        primary_key=True
    )
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. \
                 Up to 15 digits allowed."
    )
    phone_number = models.CharField(max_length=17, validators=[phone_regex])
    applying_for = models.CharField(max_length=100)
    description = models.TextField()
    watcher = models.ManyToManyField(User)
