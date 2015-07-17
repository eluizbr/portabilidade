# coding:utf-8
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView

from .models import Revenda, ContatoRevenda
from .forms import CadastroRevendaForm, ContatoRevendaFormSet


class CreateRevenda(CreateView):
    model = Revenda
    form_class = CadastroRevendaForm

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        contato_revenda_form = ContatoRevendaFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  contato_form=contato_revenda_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        contato_revenda_form = ContatoRevendaFormSet(self.request.POST)
        if (form.is_valid() and contato_revenda_form.is_valid()):
            return self.form_valid(form, contato_revenda_form)
        else:
            return self.form_invalid(form, contato_revenda_form)

    def form_valid(self, form, contato_revenda_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        contato_revenda_form.instance = self.object
        contato_revenda_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, contato_revenda_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  contato_revenda_form=contato_revenda_form))
