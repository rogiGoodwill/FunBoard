from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Ad, User
from .forms import CreateAdModelForm


# Create your views here.


class AdListView(ListView):
    template_name = 'boardApp/index.html'
    model = Ad
    context_object_name = 'ads'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdDetailView(DetailView):
    template_name = 'boardApp/ad-detail.html'
    model = Ad
    context_object_name = 'ad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class CreateAdCreateView(LoginRequiredMixin, CreateView):
    form_class = CreateAdModelForm
    template_name = 'boardApp/create-ad.html'
    success_url = '/ad/'
    # fields = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        # Мы используем ModelForm, а его метод save() возвращает инстанс
        # модели, связанный с формой. Аргумент commit=False говорит о том, что
        # записывать модель в базу рановато.
        user = User.objects.get(id=self.request.user.id)
        instance = form.save(commit=False)
        instance.user_id = user.id
        instance.save()
        instance_id = str(instance.id)
        return redirect(''.join([self.success_url, instance_id]))

class AdUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CreateAdModelForm
    template_name = 'boardApp/create-ad.html'
    context_object_name = 'ad'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return Ad.objects.get(pk=pk)

class AdDeleteView(LoginRequiredMixin, DeleteView):
    
    # def post(self, request, *args, **kwargs):
    #     user = request.user
    #
    #     new_ad = Ad
    #     #     user=user,
    #     #     text=request.get('text'),
    #     #     picture=request.get('picture'),
    #     #     videoLink=request.get('videoLink'),
    #     #     category=request.get('category'),
    #     # )
    #     new_ad.user = user
    #     new_ad.text = request.get('text')
    #     new_ad.picture = request.get('picture')
    #     new_ad.videoLink = request.get('videoLink')
    #     new_ad.category = request.get('category')








