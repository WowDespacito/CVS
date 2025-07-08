from django.db import models

# Create your models here.
# 用户表
class User(models.Model):
    username = models.CharField(max_length=20, unique=True, db_index=True, null=False, blank=False)
    password = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(max_length=128, unique=True, db_index=True)
    mobile = models.CharField(max_length=20, unique=True, db_index=True)

    name = models.CharField(max_length=20, null=False, blank=False, db_index=True)
    gender = models.CharField(max_length=1, choices=[('M','Male'),('F','Female')], default='M', null=False, blank=False)

    is_active = models.BooleanField(default=True, null=False, blank=False)
    is_admin = models.BooleanField(default=False, null=False, blank=False)
    is_teacher = models.BooleanField(default=False, null=False, blank=False)
    is_student = models.BooleanField(default=False, null=False, blank=False)

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cvs_users'
