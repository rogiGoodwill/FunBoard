from django.forms import ModelForm
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from .models import Ad, Comments


class SignUp(SignupForm):

    def save(self, request):
        user = super(SignUp, self).save(request)
        # common_group = Group.objects.get(name='common')
        # common_group.user_set.add(user)
        return user


class CreateAdModelForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'text', 'picture', 'videoLink', 'category']
        # widgets = {
        #     'title': forms.TextInput(attrs={'style': 'margin-bottom:0px'}),
        #     'text': forms.Textarea(attrs={'margin-bottom': '0px; width:100px'}),
        # }

class CreateCommentModelForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        exclude = ['user', 'ad']


