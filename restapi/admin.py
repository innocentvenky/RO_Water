from django.contrib import admin
from .models import User
from .models import Image
# Register your models here.
class Useradmin(admin.ModelAdmin):
    l=['public_id','first_name','last_name','email','phone_number','password','image']
admin.site.register(User,Useradmin)
class Imagesadmin(admin.ModelAdmin):
    l=['public_id','user_id','images']
admin.site.register(Image,Imagesadmin)