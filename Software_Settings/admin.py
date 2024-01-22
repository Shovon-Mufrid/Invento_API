from django.contrib import admin
from Software_Settings import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.module)
admin.site.register(models.sub_module)