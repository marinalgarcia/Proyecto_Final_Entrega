from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from excursiones.models import excursiones
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




# Create your views here.
#def leerexcursiones(request):
    #EXCURSIONES = excursiones.objects.all()
    
    #return render(request, 'excursiones/excursiones_list.html', {"Excursiones": EXCURSIONES})


class excursionesList(ListView):
  paginate_by = 2
  model = excursiones
  template_name = 'excursiones/excursiones_list.html'
 
  
class excursionesDetalle(DetailView):
    model=excursiones
    template_name = 'excursiones/excursiones_detalle.html'
    
class excursionesCreacion(CreateView):
    model=excursiones    
    fields = ['nombre', 'descripcion', 'precio']
    success_url = "/excursiones/Lista"
    
class excursionesUpdate(UpdateView):
    model=excursiones
    fields = ['nombre', 'descripcion', 'precio']
    success_url = "/excursiones/Lista"

class excursionesDelete(DeleteView):
    model=excursiones
    success_url = "/excursiones/Lista"
