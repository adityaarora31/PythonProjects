from django.shortcuts import render
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
    paginate_by = 2
    template_name = 'categories.html'


class ViewSpecificProperty(DetailView):
    model = Property
    template_name = 'property_detail.html'


def search_property(request):
    if request.method == 'POST':
        property_to_search = request.POST.get('search')
        city = request.POST.get('city')
        state = request.POST.get('state')
        try:
            status = Property.objects.filter(property_title__contains=property_to_search)
            status.union(Property.objects.filter(property_city__contains=city))
            status.union(Property.objects.filter(property_state__contains=state))
            if not status:
                raise Exception
            return render(request, 'search.html', {'property': status})
        except Property.DoesNotExist:
            return render(request, 'search.html', {'errors': 'Property Not Found !'})
