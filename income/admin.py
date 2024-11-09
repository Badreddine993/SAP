from django.contrib import admin
from .models import UserSource, Income

# Register your models here.
admin.site.register(Income)
admin.site.register(UserSource)