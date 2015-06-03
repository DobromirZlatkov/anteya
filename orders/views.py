from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from . import forms
from . import models
from custommixins import mixins


class OrderView(generic.View):
    template_name = 'orders/order_create.html'

    def get(self, request):
        qs = models.Product.objects.none()
        formset = forms.ProductFormSet(queryset=qs, prefix='formset')
        order_form = forms.OrderForm(prefix='order_form')
        return render(request, self.template_name, {'formset': formset, 'order_form': order_form})

    def post(self, request):
        formset = forms.ProductFormSet(request.POST, prefix='formset')
        order_form = forms.OrderForm(request.POST, prefix='order_form')
        if formset.is_valid():
            order = order_form.save()
            for form in formset.forms:
                product = form.save(commit=False)
                order.products.add(product)
                order.save()
            return HttpResponseRedirect(reverse('order_details', args=(order.id,)))
        else:
            return render(request, self.template_name, {'formset': formset, 'order_form': order_form})


class OrderDetails(generic.DetailView):
    model = models.Order
    template_name_suffix = '_details'


class OrderList(mixins.LoginRequiredMixin, mixins.AdminRequiredMixin, generic.ListView):
    model = models.Order


class OrderEdit(generic.View):
    template_name = 'orders/order_edit.html'

    def get(self, request, pk):
        order = models.Order.objects.get(pk=pk)

        formset = forms.ProductFormSet(queryset=order.products.all(), prefix='formset')

        order_form = forms.OrderForm(prefix='order_form', instance=order)
        return render(request, self.template_name, {'formset': formset, 'order_form': order_form})

    def post(self, request, pk):
        order = models.Order.objects.get(pk=pk)
        formset = forms.ProductFormSet(request.POST, prefix='formset')
        order_form = forms.OrderForm(request.POST, prefix='order_form')
        if formset.is_valid():
            order = order_form.save()
            for form in formset.forms:
                product = form.save(commit=False)
                order.products.add(product)
                order.save()
            return HttpResponseRedirect(reverse('order_details', args=(order.id,)))
        else:
            return render(request, self.template_name, {'formset': formset, 'order_form': order_form})
