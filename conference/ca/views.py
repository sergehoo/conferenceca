from django.db.models.aggregates import Sum
from ca.models import Dons, Promesse_dons
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from rest_framework.permissions import IsAuthenticated
from django_registration.backends.one_step.views import RegistrationView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    """View function for home page of site."""    
    last_dons = Dons.objects.all().order_by('-created_at')[:7]
    dernier_dons = Dons.objects.all().order_by('-created_at')[:1]
    montantrPromese = Promesse_dons.objects.all().aggregate(total_prom=Sum('cathegorie'))
    montantDons = Dons.objects.all().aggregate(total_amount=Sum('montant'))
   # num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
   # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
   # num_authors = Author.objects.count()

    context = {
       'last_dons': last_dons,
       'dernier': dernier_dons,
        'dons': montantDons,
        'promesse': montantrPromese,
        #'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'ca/index.html', context=context)

@login_required
def dashboardview(request):
    """View function for home page of site."""    
   

    # Generate counts of some of the main objects
    last_dons = Dons.objects.all().order_by('-created_at')
   # num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
   # num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
   # num_authors = Author.objects.count()

    context = {
       'last_dons': last_dons,
        #'num_instances': num_instances,
        #'num_instances_available': num_instances_available,
        #'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'ca/index.html', context=context)


class RegistrationView(RegistrationView):
    success_url = reverse_lazy('dashboard:dashboard') 