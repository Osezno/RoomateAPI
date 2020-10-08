from django.db import models
import uuid
# Create your models here.


class Roles(models.Model):
    codigo = models.CharField(max_length=30)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta:
        db_table = "roles"


class Estatus(models.Model):
    codigo = models.CharField(max_length=30)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta:
        db_table = "estatus"

class Usuario(models.Model):
    
    id_rol = models.IntegerField()
    id_estatus = models.IntegerField()
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    uuid = models.CharField(default=uuid.uuid4,max_length=255, editable=False, unique=True)
    tmp_password = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    fotografia = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    ses_id = models.CharField(max_length=255)
    onboard   = models.BooleanField(choices=((False, False),(True, True)))
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True, editable=False)
    
    class Meta:
        db_table = "usuarios"

    
