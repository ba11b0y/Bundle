from django.contrib import admin
from .models import User, Goal, GS


# Register your models here.

admin.site.register(User)
admin.site.register(Goal)
admin.site.register(GS)
