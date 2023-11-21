# from django.db import models
# from django.contrib.auth.models import AbstractUser 


# class MyUser(AbstractUser):
#     REQUIRED_FIELDS =  ["first_name","last_name","email"]
#     STATUS = (
#         ("admin","ADMIN"),
#         ("assis","ASSISTANT"),
#         ("teacher","TEACHER"),
#         ("user","USER")
#     )
#     status = models.CharField(max_length=50,choices=STATUS, default="user")
#     fan = models.CharField(max_length=50,default="")
#     gruhi = models.CharField(max_length=50,default="")
    
# class Student(models.Model):  
#     ism = models.CharField(max_length=50)
#     familya = models.CharField(max_length=50)
#     tel = models.CharField(max_length=50)
#     vaqt = models.CharField(max_length=50)
#     kun = models.CharField(max_length=50)

# class Gruhlar(models.Model):
#     yunalishi = models.CharField(max_length=50)
#     vaqt =models.CharField(max_length=50)
#     teacher = models.ForeignKey(MyUser, on_delete=models.CASCADE)
from django.contrib.auth.models import AbstractUser
from django.db import models

class MyUser(AbstractUser):
    ROLE_USER = 'admin'
    ROLE_ASSISTANT = 'assistant'
    ROLE_TEACHER = 'teacher'

    ROLE_CHOICES = [
        (ROLE_USER, 'Admin'),
        (ROLE_ASSISTANT, 'Yordamchi'),
        (ROLE_TEACHER, 'O\'qituvchi'),
    ]
    REQUIRED_FIELDS = ["first_name","last_name"]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_USER)

    if role == ROLE_TEACHER:
        fan = models.CharField(max_length=100, blank=True, null=True, verbose_name='Fan')
        gruhi = models.CharField(max_length=100, blank=True, null=True, verbose_name='Gruhi')

    def __str__(self):
        return f"{self.get_role_display()} - {self.username}"

class Student(models.Model):
    ismi = models.CharField(max_length=50)
    familya = models.CharField(max_length=50)
    yunalish = models.CharField(max_length=50)
    vaqt = models.CharField(max_length=50)
    kun = models.CharField(max_length=50)
    telefon = models.CharField(max_length=11)

class Yunalishlar(models.Model):
    nomi = models.CharField(max_length=50)
    def __str__(self):
        return self.nomi
    