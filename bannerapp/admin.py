from django.contrib import admin

# Register your models here.
from .models import *

class banner_uploadAdmin(admin.ModelAdmin):
    list_display = ['pub_name','banner_name']

class client_signupAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','mobile']

class publisher_signupAdmin(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','mobile']

admin.site.register(banners_upload,banner_uploadAdmin)
admin.site.register(client_signup,client_signupAdmin)
admin.site.register(publisher_signup,publisher_signupAdmin)