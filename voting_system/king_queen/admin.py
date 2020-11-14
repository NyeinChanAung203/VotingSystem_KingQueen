from django.contrib import admin
from .models import FirstYear,TheWhole
# Register your models here.

@admin.register(FirstYear)
class FirstYearAdmin(admin.ModelAdmin):
    list_display = ['name','gender','votes']
    list_filter = ['gender','votes']

    def get_ordering(self,request):
        return ['-votes']


@admin.register(TheWhole)
class TheWholeAdmin(admin.ModelAdmin):
    list_display = ['name','gender','votes']
    list_filter = ['gender','votes']

    def get_ordering(self,request):
        return ['-votes']