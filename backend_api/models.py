
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.
# USER MODELS MAIN

class UserManager(BaseUserManager):
    def _create_user(self, username, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        return self._create_user(username, password, True, True, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    idUser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        
    USERNAME_FIELD = 'username'
    objects = UserManager()
    def __str__(self):
        return   "%s (%s)" % (
            self.idUser,
            self.username,
        )
# MODELS FOR AUTHENTICATION  MAYBE


class UsersAuth(models.Model):
    idUserAuth = models.OneToOneField(
        Users,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    token = models.CharField(max_length=255)

