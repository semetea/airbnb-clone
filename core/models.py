from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)  # auto_now_add 새로 만들면 그 시간을 저장
    updated = models.DateTimeField(auto_now=True)  # 모델이 저장될 때마다 시간 기록

    class Meta:
        abstract = True  # abstract model은 데이터베이스에 등록되지 않는다
