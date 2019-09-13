from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accionista.models import Accionista
from django.shortcuts import get_object_or_404
from django.db.models import Q

class AccionistasView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    queryset = request.GET.get("Buscar")
    accionistas = Accionista.accionistas.all()
    if queryset:
      accionistas = Accionista.accionistas.filter(
        Q( nombres__icontains = queryset) |
        Q( apellidos__icontains = queryset)
      ).distinct()
    return render(request, 'accionistas.html', {'accionistas' : accionistas})

class CreateAccionista(LoginRequiredMixin, CreateView):
  model = Accionista
  template_name = './crear.html'
  fields = '__all__'

class UpdateAccionista(LoginRequiredMixin, UpdateView):
  model = Accionista
  template_name = './editar.html'
  fields = ['nombres', 'apellidos', 'totalAcciones', 'nacionalidad', 'direccion', 'telefono', 'email', 'fax']

class DetalleAccionistaView(LoginRequiredMixin, TemplateView):
  def get(self, request, **kwargs):
    id=kwargs["pk"]
    print(id)
    return render(request, 'accionista.html', {'accionista' : Accionista.accionistas.get(id=id)})

