from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from forms import ProductFormSet, OrderForm
from . import models
from custommixins import mixins


class OrderView(generic.View):
    template_name = 'orders/order_create.html'

    def get(self, request):
        formset = ProductFormSet(prefix='formset')
        order_form = OrderForm(prefix='order_form')
        return render(request, self.template_name, {'formset': formset, 'order_form': order_form})

    def post(self, request):
        formset = ProductFormSet(request.POST, prefix='formset')
        order_form = OrderForm(request.POST, prefix='order_form')
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
    #template_name = "orders/order_details.html"
    template_name_suffix = '_details'

    # def get_context_data(self, **kwargs):
    #     context = super(OrderDetails, self).get_context_data(**kwargs)
    #     context['total'] = self.total_amount
    #     return context


class OrderList(mixins.LoginRequiredMixin, mixins.AdminRequiredMixin, generic.ListView):
    model = models.Order
