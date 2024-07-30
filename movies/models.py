from django.db import models

# Create your models here.
class Movie(models.Model):

    CATEGORY_CHOICES = [
        ('좋아요', '좋아요'),
        ('보통', '보통'),
        ('싫어요', '싫어요'),
    ]

    title = models.CharField(max_length=100, primary_key=True)
    summary = models.TextField(null=True, blank=True)  
    #두가지 중에 하나만 입력받을 수 있음
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

    
    