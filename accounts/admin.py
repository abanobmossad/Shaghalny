from django.contrib import admin

# Register your models here.
from accounts.models import User,Company,UserProfile

admin.site.register(User)
admin.site.register(Company)
admin.site.register(UserProfile)