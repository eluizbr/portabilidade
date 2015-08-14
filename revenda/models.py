# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User
from port.models import Cadastro


class Codigo_revenda(models.Model):
    revenda = models.CharField(u'Codigo da Revenda',max_length=100, unique=True, default=0)
    cliente = models.ForeignKey(Cadastro)
