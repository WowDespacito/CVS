from django.db import models

# Create your models here.
# 用户表
class User(models.Model):
    username = models.CharField(max_length=20, unique=True, db_index=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=128, unique=True, db_index=True, blank=True)
    mobile = models.CharField(max_length=20, unique=True, db_index=True, blank=True)

    name = models.CharField(max_length=20, db_index=True)
    gender = models.CharField(max_length=1, choices=[('M','Male'),('F','Female')], default='M')

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cvs_users'
