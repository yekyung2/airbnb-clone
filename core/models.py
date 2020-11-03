from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Model Definition"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

# 위의 데이터를 데이터베이스로 보내지 않고 싶을 때, abstract(추상모델)을 사용한다.
    class Meta:
        abstract = True
