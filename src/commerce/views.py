from django.shortcuts import render


def welcome_page(request):
    return render(request, 'commerce/main.html')
