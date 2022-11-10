from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from excursiones.models import Excursiones
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import   DetailView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.template import loader
# Create your views here.

class ExcursionesList(ListView):
  paginate_by = 2
  model = Excursiones
  template_name = 'excursiones/excursiones_list.html'
 
  
class ExcursionesDetalle(DetailView):
    model=Excursiones
    template_name = 'excursiones/excursiones_detalle.html'
    
class ExcursionesCreacion(CreateView):
    model=Excursiones    
    fields = ['nombre', 'descripcion', 'precio']
    success_url = "/excursiones/lista"
    
class ExcursionesUpdate(UpdateView):
    model=Excursiones
    fields = ['nombre', 'descripcion', 'precio']
    success_url = "/excursiones/lista"

class ExcursionesDelete(DeleteView):
    model=Excursiones
    success_url = "/excursiones/lista"
