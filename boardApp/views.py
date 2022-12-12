from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Ad, User, Category, Comments
from .forms import CreateAdModelForm, CreateCommentModelForm
from .filters import CommentFilter


class AdListView(ListView):
    """
    Представление показывает все объявления
    """
    template_name = 'boardApp/index.html'
    model = Ad
    context_object_name = 'ads'
    paginate_by = 3
    queryset = Ad.objects.all().order_by('-published_date')

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
        context['user_login'] = self.request.user
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


class CommentAdCreateView(LoginRequiredMixin, CreateView):
    """
    Представление создания комментария к объявлению
    """
    model = Comments
    form_class = CreateCommentModelForm
    template_name = 'boardApp/create-comment.html'
    success_url = '/ad/'
    context_object_name = 'comment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ad'] = Ad.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        # Мы используем ModelForm, а его метод save() возвращает инстанс
        # модели, связанный с формой. Аргумент commit=False говорит о том, что
        # записывать модель в базу рановато.
        user = User.objects.get(id=self.request.user.id)
        ad = Ad.objects.get(id=self.kwargs.get('pk'))
        instance = form.save(commit=False)
        instance.user_id = user.id
        instance.ad_id = ad.id
        instance.save()
        instance_id = str(instance.ad_id)
        return redirect(''.join([self.success_url, instance_id]))


class MyCommentsListView(ListView):
    """
    Представление показывает мои отзывы
    """
    template_name = 'boardApp/show-comments.html'
    model = Comments
    context_object_name = 'comments'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CommentFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        user = self.request.user
        return Comments.objects.filter(ad__user=user).order_by('-published_date')


class CommentDetailView(LoginRequiredMixin, DetailView):
    """
    Представление показывает выбранный отзыв
    """
    template_name = 'boardApp/comment-detail.html'
    model = Comments
    context_object_name = 'comment'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_login'] = self.request.user
        return context


class CommentDeleteView(DeleteView):
    """
    Представление удаляет отзыв
    """
    template_name = 'boardApp/comment-delete.html'
    context_object_name = 'comment'
    queryset = Comments.objects.all()
    success_url = '/comments/'


def create_default_categories():
    """
    Процедура создания категорий.
    Выполняется в случае, если список категорий пуст.
    """

    categories = ['Танки', 'Хиллы', 'DD', 'Торговцы', 'Гилдмастеры', 'Квестгиверы',
                  'Кузнецы', 'Кожевники', 'Зельевары', 'Мастеры заклинаний']
    for cat in categories:
        Category.objects.create(category=cat)


def comment_accepted_send_email(request, pk):
    comments = Comments.objects.get(pk=pk)
    comments.is_accepted = True
    comments.save()
    comment_text = comments.comment
    comment_pk = comments.pk
    ad_title = comments.ad.title

    email = User.objects.get(pk=comments.user.pk).email
    username = User.objects.get(pk=comments.user.pk)

    html_content = render_to_string(
        'boardApp/comment_accept.html',
        context=
        {'ad_title': ad_title,
         'comment_text': comment_text,
         'username': username,
         'comment_pk': comment_pk,
         'domain_url': settings.DOMAIN, }
    )

    msg = EmailMultiAlternatives(
        subject='Новый отзыв',
        from_email='django.testemail@yandex.ru',
        to=[email, ]
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()

    return redirect('/comments/')
