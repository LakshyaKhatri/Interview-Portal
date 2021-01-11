from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator


class Technology(models.Model):
    """
    Technology Model: Contains all the technologies to be
    used by other models. This model should be treated as a pool
    for available technologies.
    """
    class Meta:
        verbose_name_plural = "technologies"

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Status(models.Model):
    """
    Status Model: Contains all the `Status` that an
    application can have. This model should be treated as
    a pool for available status options.
    """
    class Meta:
        verbose_name_plural = "status"

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Application(models.Model):
    """
    Application Model: Contains the basic information for
    a registered application. All of the fields can be used
    frequently in list views and hence kept together. The detailed
    information for a single application can be requested along
    with the `ApplicationDetail` model.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    TYPE_CHOICES = [('CL', 'Client'), ('CA', 'Candidate')]
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='CA')
    technology = models.ForeignKey('Technology', on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    applied_on = models.DateTimeField(auto_now_add=True)
    moved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ApplicationDetail(models.Model):
    """
    Application Detail Model: This model will contain additional
    detail for a single application the model is created with and
    intent to pass detailed information for a single Application
    rather than being used in lists views.
    """
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
    watchers = models.ManyToManyField(User)
