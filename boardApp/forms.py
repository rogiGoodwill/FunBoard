from django.forms import ModelForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from .models import Ad


class SignUp(SignupForm):

    def save(self, request):
        user = super(SignUp, self).save(request)
        # common_group = Group.objects.get(name='common')
        # common_group.user_set.add(user)
        return user


class CreateAdModelForm(ModelForm):
    class Meta:
        model = Ad
        fields = ['text', 'picture', 'videoLink', 'category']



