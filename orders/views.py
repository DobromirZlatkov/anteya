from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render

from forms import ProductFormSet


class OrderView(generic.View):
    template_name = 'orders/order_create.html'

    def get(self, request):
        formset = ProductFormSet()
        return render(request, self.template_name, {'formset': formset})

    def post(self, request):
        formset = ProductFormSet(request.POST)
        print formset.is_valid()
        if formset.is_valid():
            # for form in formset.forms:
            #     print "You've picked {0}".format(form.cleaned_data['color'])

            return redirect('success')
        else:
               # Invalid form! Reshow the form with error highlighted
            return render(request, self.template_name, {'formset': formset})

