from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm
from django.http import HttpResponse
from .models import Teacher, Course, ClassNumber, Subject


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


def get_base_context():
    menu = [
        {'link': '/info', 'text': 'Информация'},
        {'link': '/courses', 'text': 'Курсы'},
        {'link': '/main', 'text': 'Главная'},
        {'link': '/teachers', 'text': 'Учителя'},
    ]

    courses = Course.objects.all()

    return {
        'menu': menu,
        'courses': courses,
    }


def show_stream(request):
    context = get_base_context()
    return render(request, 'stream.html', context)


def show_main(request):
    context = get_base_context()
    return render(request, 'mainpage.html', context)


def show_courses(request):
    context = get_base_context()
    courses = Course.objects.all()
    context['courses'] = courses
    return render(request, 'courses.html', context)


def show_course(request):
    return render(request, 'course.html')


def show_info(request):
    context = get_base_context()
    return render(request, 'infopage.html', context)


def show_teachers(request):
    context = get_base_context()
    return render(request, 'teachers.html', context)