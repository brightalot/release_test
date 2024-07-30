from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
		# 관리자 페이지의 테이블에서 볼 수 있는 필드
    list_display = ("code", "name", "gender")