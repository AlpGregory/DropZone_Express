from django.shortcuts import render, redirect
from auth_and_perms.forms import NewUserForm, LoginUserForm


def signup_client(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()

    return redirect('auth_and_perms.login')


def login(request):
    return render(request, 'auth_and_perms/login.html')
