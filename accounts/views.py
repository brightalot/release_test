from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from .forms import SignupForm

User = get_user_model()

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # 회원가입 후 자동 로그인
        return redirect(self.success_url)
