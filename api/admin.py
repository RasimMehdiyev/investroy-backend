from django.contrib import admin
from .models import *
# Register your models here.
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title' , 'author' , 'created_at' , 'updated_at']
admin.site.register(BlogModel , BlogModelAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'created_at']
admin.site.register(ContactUs , ContactUsAdmin)