from datetime import datetime, date

from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, get_user
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils import timezone

from .forms import CustomUserCreationForm
from articles.models import Article


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'
    

# class UserDetailView(UserPassesTestMixin, DetailView):
class UserDetailView(DetailView):
    template_name = 'users/user_detail.html'
    model = get_user_model()
    context_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.user = context['object']
        context['auth_user'] = get_user(self.request)
        context['age'] = self.get_user_age()
        context['articles'] = self.last_user_articles()
        return context

    def get_user_age(self):
        birth_date = self.user.birth_date
        now = timezone.localdate()
        # Take leap years into account
        res = int((now - birth_date).days // 365.25) if birth_date else 'Не указан'
        return res

    def last_user_articles(self):
        article_list = Article.objects.all().filter(author=self.user)
        return article_list[:5]



class UserUpdateView(UserPassesTestMixin, UpdateView):
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


    def test_func(self):
        return self.get_object() == self.request.user

    def get_success_url(self) -> str:
        return reverse_lazy('user_detail', kwargs={'pk': self.request.user.pk})

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)