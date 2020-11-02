from django.contrib import admin
from . import models

# Register your models here.


# admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    list_display = ("username", "gender", "language", "currency", "superhost")
