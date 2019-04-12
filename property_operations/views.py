from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, UpdateView, ListView, DetailView
from django.contrib.auth.models import User
import smtplib
from login.models import RegisterUser
from .forms import PropertyForm
from .models import Property, Enquiry
PASSWORD = "@dity@@ror@31"


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

    # def post(self, *args):
    #     import pdb;pdb.set_trace()
    #     return


# def handle_query(self, request):
#         query = Enquiry()
#         current_user = User.objects.get(pk=self.id)
#         query.mail = current_user.user_email


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


def property_view(request):
    user = RegisterUser.objects.get(username=request.user)
    if request.method == 'GET' and user.is_seller:
        try:
            property = Property.objects.filter(property_seller_name=request.user)
            return render(request, 'seller_property.html', {'property': property, 'is_seller': True})
        except Property.DoesNotExist:
            return render(request, 'seller_property.html', {'property': "You have not posted any property !",
                                                            'is_seller': True})


def make_query(request, pid):
    try:
        enq = Enquiry()
        enq.enquiry_property = Property.objects.get(id=pid)
        enq.enquiry_person = RegisterUser.objects.get(username=request.user)
        enq.enquiry_description = request.POST.get('Query')
        EMAIL_ADDRESS = "aditya.arora@tothenew.com"
        property_seller_email = RegisterUser.objects.get(id=pid).user_email
        import pdb;
        pdb.set_trace()
        enq.save()
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(enq.enquiry_property.property_title, enq.enquiry_description)
        server.sendmail(EMAIL_ADDRESS, property_seller_email, message)
        server.quit()
        print("Success: Email sent!")
    except:
        return HttpResponse("Email failed to send.")
    return redirect('/view_property/', id=pid)
