from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import FormView, UpdateView, ListView, DetailView
from django.contrib.auth.models import User
from .forms import PropertyForm
from .models import Property


class PropertyOperations(FormView):

    form_class = PropertyForm
    template_name = 'property_form.html'

    def form_valid(self, form):
        if self.request.session['is_seller']:
            user_id = User.objects.get(username=self.request.session['present_user'])
            form.instance.property_seller_name = user_id
            form.save()
            message = 'You have successfully posted a property !'
            return render(self.request, template_name='property_form.html', context={'message': message})

        else:
            message = 'You cannot post a property since you are not a seller !'
            return render(self.request, template_name='property_form.html', context={'message': message})

    def form_invalid(self, form):
        return render(self.request, template_name='property_form.html', context={'form': form.errors})


class UpdateProperty(UpdateView):
    model = Property
    fields = ['property_title', 'property_address', 'property_city', 'property_state', 'property_pin',
              'property_price', 'property_bedroom', 'property_bathroom', 'property_sq_feet', 'property_lot_size',
              'property_garage', 'property_description', 'property_image', 'property_image2', 'property_image3',
              'property_image4']
    template_name = 'update_property.html'


class ViewProperty(ListView):
    model = Property
    paginate_by = 1
    template_name = 'property_list.html'


class ViewSpecificProperty(DetailView):
    model = Property
    template_name = 'property_detail.html'
