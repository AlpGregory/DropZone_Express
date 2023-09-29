from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from auth_and_perms.forms import ClientSignUpForm
from auth_and_perms.models import User


class ClientSignUpView(CreateView):
    model = User
    form_class = ClientSignUpForm
    template_name = 'auth_and_perms/signup_form.html'
    success_url = reverse_lazy('commerce:welcome_page')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('commerce:welcome_page')


def signup(request):
    return render(request, 'auth_and_perms/signup.html')


def seller_signup(request):
    pass


def admin_signup(request):
    pass


def login_view(request):
    return render(request, 'auth_and_perms/login.html')
