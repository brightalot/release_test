from django.contrib import admin
from .models import Movie

# Register your models here.
# Register your models here.
@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
		# 관리자 페이지의 테이블에서 볼 수 있는 필드
    list_display = ("title", "summary", "category")