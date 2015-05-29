from django.views import generic
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.core.urlresolvers import reverse

from rolepermissions.mixins import HasRoleMixin

from custommixins import mixins

from . import forms
from . import models


# class Company(generic.TemplateView):
#     template_name = 'companies/index.html'


class CompanyList(mixins.LoginRequiredMixin, generic.ListView):
    model = models.Company

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CompanyList, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        user = self.request.user
        context['object_list'] = user.companies.all()
        return context


class CompanyCreate(mixins.LoginRequiredMixin, generic.edit.CreateView):
    model = models.Company
    valid_message = "Successfully created object."

    # success_url = reverse_lazy('companies', kwargs={'id': request.user.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CompanyCreate, self).form_valid(form)

    def get_form_class(self):
        return forms.CompanyForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('companies', kwargs={'id': self.request.user.id})


class CompanyEdit(generic.edit.UpdateView):
    model = models.Company
    template_name_suffix = '_update'

    def get_form_class(self):
        return forms.CompanyForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('companies', kwargs={'id': self.request.user.id})


class CompanyDelete(generic.edit.DeleteView):
    model = models.Company
    template_name_suffix = '_delete'

    def get_success_url(self, **kwargs):
        return reverse_lazy('companies', kwargs={'id': self.request.user.id})
