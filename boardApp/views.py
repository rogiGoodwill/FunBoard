from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Ad
from .forms import CreateAdModelForm


# Create your views here.


class IndexListView(ListView):
    template_name = 'boardApp/index.html'
    model = Ad

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateAdCreateView(CreateView, LoginRequiredMixin):
    form_class = CreateAdModelForm
    template_name = 'boardApp/create-ad.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        user = request.user

        new_ad = Ad.objects.create(
            user=user,
            text=request.get('text'),
            picture=request.get('picture'),
            videoLink=request.get('videoLink'),
            category=request.get('category'),
        )
        return new_ad.save()





