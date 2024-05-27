from django.contrib import admin
from .models import Task
# Register your models here.
class myadmin(admin.ModelAdmin):
    list_display=("field1","priority")
    search_fields=['field1']
admin.site.register(Task,myadmin)