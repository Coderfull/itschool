from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     model = MyUser
#     if MyUser.status == "assis":
#         list_filter = ['last_name']
#         list_display = ['last_name','username','is_staff','status']
#     elif MyUser.status == "teacher":
#         list_display = ['last_name','username','is_staff','fan','gruhi']
#     else:
#         list_display = ['last_name','username','is_staff' ]


# admin.site.register(MyUser)
# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser,Student,Yunalishlar

admin.site.register(MyUser)
admin.site.register(Student)
admin.site.register(Yunalishlar)
