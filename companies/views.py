from django.views import generic
from django.core.urlresolvers import reverse_lazy

from custommixins import mixins

from . import forms
from . import models


# class Company(generic.TemplateView):
#     template_name = 'companies/index.html'


class CompanyList(mixins.LoginRequiredMixin, generic.ListView):
    model = models.Company

    def get_context_data(self, **kwargs):
        context = super(CompanyList, self).get_context_data(**kwargs)
        user = self.request.user
        context['object_list'] = user.companies.all()
        return context


class CompanyCreate(mixins.LoginRequiredMixin, generic.edit.CreateView):
    model = models.Company
    valid_message = "Successfully created object."
    form_class = forms.CompanyForm
    # success_url = reverse_lazy('companies', kwargs={'id': request.user.id})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CompanyCreate, self).form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse_lazy('companies', kwargs={'id': self.request.user.id})


class CompanyEdit(mixins.LoginRequiredMixin, generic.edit.UpdateView):
    model = models.Company
    template_name_suffix = '_update'
    form_class = forms.CompanyForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('companies', kwargs={'id': self.request.user.id})


class CompanyDelete(mixins.LoginRequiredMixin, generic.edit.DeleteView):
    model = models.Company
    template_name_suffix = '_delete'

    def get_success_url(self, **kwargs):
        return reverse_lazy('companies', kwargs={'id': self.request.user.id})
