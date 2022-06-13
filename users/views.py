from datetime import datetime, date

from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from .forms import CustomUserCreationForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    

class UserDetailView(DetailView):
    template_name = 'users/user_detail.html'
    model = get_user_model()
    context_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = get_user(self.request)
        context['auth_user'] = user
        context['age'] = self.get_user_age()
        print('='*30)
        print(user.avatar)
        print(user.avatar.path)
        print(user.avatar.url)
        print('='*30)
        return context

    def get_user_age(self):
        user = get_user(self.request)
        birth_date = user.birth_date
        now = timezone.localdate()
        # Take leap years into account
        res = int((now - birth_date).days // 365.25) if birth_date else 'Не указан'
        return res


class UserUpdateView(LoginRequiredMixin, UpdateView):
    # form_class = CustomUserChangeForm
    model = get_user_model()
    context_name = 'user'
    template_name = 'users/user_update.html'
    fields = [
        'avatar',
        'first_name', 
        'last_name',
        'birth_date',
        'sex']
    # fields = '__all__'
    login_url = 'login'

    def test_func(self):
        user = self.get_object()
        return user == self.request.user

    def get_success_url(self) -> str:
        return reverse_lazy('user_detail', kwargs={'pk': self.request.user.pk})

    def post(self, request, *args, **kwargs):
        file = request.FILES['avatar']
        print('='*30)
        # print(file.width, file.height)
        print('='*30)
        return super().post(request, *args, **kwargs)