from django.contrib import admin
from .models import State, National, Professional

# Register your models here.
admin.site.register(State)
admin.site.register(National)
admin.site.register(Professional)