from django.shortcuts import render
from django.views import generic
from .models import Objeto
# Create your views here.
class PrincipalView(generic.ListView):
    template_name = "principal.html"
    def get_queryset (self):
        toggle = self.request.GET.get('toggle')
        if toggle:
            aux = Objeto.objects.get(pk=toggle)
            valor = aux.cont
            new_valor = valor + 1
            Objeto.objects.filter(pk=toggle).update(cont = new_valor)
        return Objeto.objects.all().distinct()
    

class LandingView(generic.TemplateView):
    template_name = "landing.html"