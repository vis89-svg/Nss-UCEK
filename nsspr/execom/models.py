from django.db import models

# Create your models here.
class execom(models.Model):
    execom=models.CharField(max_length=50)
    volntsecr=models.CharField(max_length=50)
    volntsecrimg1=models.ImageField(upload_to="pic")
    volntsecrname1=models.CharField(max_length=50)
    volntsecrimg2=models.ImageField(upload_to="pic")
    volntsecrname2=models.CharField(max_length=50)
    jointsecr=models.CharField(max_length=50)
    jointsecrimg1=models.ImageField(upload_to="pic")
    jointsecrname1=models.CharField(max_length=50)
    jointsecrimg2=models.ImageField(upload_to="pic")
    jointsecrname2=models.CharField(max_length=50)
    campsecr=models.CharField(max_length=50)
    campsecrimg1=models.ImageField(upload_to="pic")
    campsecrname1=models.CharField(max_length=50)
    campsecrimg2=models.ImageField(upload_to="pic")
    campsecrname2=models.CharField(max_length=50)
    execmem=models.CharField(max_length=50)
    execmemgrp1=models.CharField(max_length=50)
    execmemimg1=models.ImageField(upload_to="pic")
    execmemname1=models.CharField(max_length=50)
    execmemgrp2=models.CharField(max_length=50)
    execmemimg2=models.ImageField(upload_to="pic")
    execmemname2=models.CharField(max_length=50)
    execmemgrp3=models.CharField(max_length=50)
    execmemimg3=models.ImageField(upload_to="pic")
    execmemname3=models.CharField(max_length=50)
    execmemgrp4=models.CharField(max_length=50)
    execmemimg4=models.ImageField(upload_to="pic")
    execmemname4=models.CharField(max_length=50)
    execmemgrp5=models.CharField(max_length=50)
    execmemimg5=models.ImageField(upload_to="pic")
    execmemname5=models.CharField(max_length=50)
    def __str__(self):
        return self.execom
