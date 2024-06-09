from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Categoria


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias.html'


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoriaDetail.html'
    context_object_name = 'categoria'


def home(request):
    return render(request, 'home.html')


