from django.db import models

class Configuration(models.Model):
    nbgrp = models.IntegerField()
    nbusr = models.IntegerField()
    minmax = models.IntegerField()

class Usrs(models.Model):
    idusr = models.IntegerField(primary_key=True)
    nameusr = models.CharField(max_length=255)

    idgrp = models.ForeignKey('Grp', models.SET_NULL,
    blank=True,
    null=True,)

class Grp(models.Model):
    idgrp = models.IntegerField(primary_key=True)
    namegrp = models.CharField(max_length=255)
    islast = models.IntegerField()


