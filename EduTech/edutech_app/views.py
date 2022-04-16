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


def show_stream(request):
    return render(request, 'stream.html')


def show_main(request):
    return render(request, 'mainpage.html')


def show_courses(request):
    return render(request, 'courses.html')


def show_info(request):
    return render(request, 'infopage.html')


def show_teachers(request):
    return render(request, 'teachers.html')
