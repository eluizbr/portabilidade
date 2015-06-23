from django import forms
from models import Cadastro

class CadastroFrom(forms.ModelForm):
	class Meta:
		model = Cadastro
		fields = ['user','tipo','cpf','cnpj','ie','telefoneF','telefoneM','email',
				'email_contato','nome','endereco','numero','bairro','complemento',
				'cidade','estado','cep','cod_cliente','plano']
		