# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.

class PostOfficeEmailtemplate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    subject = models.CharField(max_length=255)
    content = models.TextField()
    html_content = models.TextField()
    created = models.DateTimeField()
    last_updated = models.DateTimeField()

    def __unicode__(self):
    	return unicode(self.name)

    class Meta:
        managed = False
        db_table = 'post_office_emailtemplate'



class envio(models.Model):

	TIPO_CHOICES = (
	    (u'Parceiro', 'Parceiro'),
	    (u'Cliente', 'Cliente')
	)

	nome = models.CharField(max_length=255)
	telefone = models.CharField(max_length=25,default='(00)0000-0000')
	email = models.EmailField(unique=True)
	empresa = models.CharField(max_length=255)
	data = models.DateTimeField(auto_now_add=True)
	enviado = models.IntegerField(default=0)
	tipo = models.CharField(max_length=25,choices=TIPO_CHOICES,default='Parceiro')
	template = models.ForeignKey('PostOfficeEmailtemplate',default=11)
