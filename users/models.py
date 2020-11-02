from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


# default="" or null=True
class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGES_ENGLISH = "en"
    LANGUAGES_KOREAN = "kr"

    LANGUAGES_CHOICES = [
        (LANGUAGES_ENGLISH, 'English'),
        (LANGUAGES_KOREAN, 'Korean'),
    ]

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = [
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW")
    ]

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, null=True, blank=True)
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGES_CHOICES, max_length=2, null=True, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True)
    superhost = models.BooleanField(default=False)
