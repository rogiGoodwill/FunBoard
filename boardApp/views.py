from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Ad, User, Category
from .forms import CreateAdModelForm


# Create your views here.


class AdListView(ListView):
    """
    Представление показывает все объявления
    """
    template_name = 'boardApp/index.html'
    model = Ad
    context_object_name = 'ads'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AdDetailView(DetailView):
    """
    Представление показывает выбранное объявление
    """
    template_name = 'boardApp/ad-detail.html'
    model = Ad
    context_object_name = 'ad'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreateAdCreateView(LoginRequiredMixin, CreateView):
    """
    Представление создает объявление
    """
    model = Ad
    form_class = CreateAdModelForm
    template_name = 'boardApp/create-ad.html'
    success_url = '/ad/'
    context_object_name = 'ad'

    # fields = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Проверяем, существуют ли категории,
        # и создаем дефолтные категории, если они не существуют
        if not Category.objects.count():
            create_default_categories()
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
    """
    Представление обновляет содержение объявления
    """
    form_class = CreateAdModelForm
    template_name = 'boardApp/create-ad.html'
    context_object_name = 'ad'
    success_url = '/'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        return Ad.objects.get(pk=pk)


class AdDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление удаляет объявление
    """
    template_name = 'boardApp/ad-delete.html'
    context_object_name = 'ad'
    queryset = Ad.objects.all()
    success_url = '/'


def create_default_categories():
    """
    Процедура создания категорий.
    Выполняется в случае, если список категорий пуст.
    """
    Category.objects.create(category='Танки')
    Category.objects.create(category='Хиллы')
    Category.objects.create(category='DD')
    Category.objects.create(category='Торговцы')
    Category.objects.create(category='Гилдмастеры')
    Category.objects.create(category='Квестгиверы')
    Category.objects.create(category='Кузнецы')
    Category.objects.create(category='Кожевники')
    Category.objects.create(category='Зельевары')
    Category.objects.create(category='Мастеры заклинаний')
