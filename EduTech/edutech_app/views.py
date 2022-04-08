from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm
from django.http import HttpResponse


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def get_base_context(pagename):
    menu = [
        {'link': '/info', 'text': 'Информация'},
        {'link': '/courses', 'text': 'Курсы'},
        {'link': '/main', 'text': 'Главная'},
        {'link': '/teachers', 'text': 'Учителя'},
    ]

    return {
        'pagename': pagename,
        'menu': menu,
    }


def show_stream(request):
    context = get_base_context('c')
    return render(request, 'Stream/stream.html', context)


def show_main(request):
    context = get_base_context('c')
    return render(request, 'mainpage.html', context)


def show_courses(request):
    context = get_base_context('c')
    return render(request, 'courses.html', context)


def show_info(request):
    context = get_base_context('c')
    return render(request, 'infopage.html', context)


def show_teachers(request):
    context = get_base_context('c')
    return render(request, 'teachers.html', context)
