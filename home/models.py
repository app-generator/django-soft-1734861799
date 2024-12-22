# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    codice_riga = models.CharField(max_length=255, null=True, blank=True)
    codice_agenzia = models.CharField(max_length=255, null=True, blank=True)
    data_inizio_mandato = models.DateTimeField(blank=True, null=True, default=timezone.now)
    nome_agenzia = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Agenti_Db(models.Model):

    #__Agenti_Db_FIELDS__
    codice_riga = models.CharField(max_length=255, null=True, blank=True)
    codice_agenzia = models.CharField(max_length=255, null=True, blank=True)
    data_inizio_mandato = models.DateTimeField(blank=True, null=True, default=timezone.now)
    nome_agenzia = models.TextField(max_length=255, null=True, blank=True)

    #__Agenti_Db_FIELDS__END

    class Meta:
        verbose_name        = _("Agenti_Db")
        verbose_name_plural = _("Agenti_Db")



#__MODELS__END
