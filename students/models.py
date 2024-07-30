from django.db import models

# Create your models here.
class Student(models.Model):
	# 범주형 데이터를 표현
	# male, female만 입력 값으로 받음
	# male, female은 데이터베이스에 저장되는 형식
	# 남자, 여자는 우리에게 보여지는 형식
    gender_choices = [
        ("male", "남자"),
        ("female", "여자"),
    ]

    code = models.CharField(max_length=10, primary_key=True) #주키
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    #두가지 중에 하나만 입력받을 수 있음
    gender = models.CharField(max_length=10, choices=gender_choices)
    info = models.TextField(null=True, blank=True)