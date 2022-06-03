from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm
from django.http import HttpResponseRedirect
from .models import Course, CurrentCourse


def get_base_context(user_is_authed):
    context = {
        'courses': Course.objects.all(),
    }
    if not user_is_authed:
        buttons = {
            '/accounts/register': 'sign up',
            '/accounts/login': 'sign in',
        }
    else:
        buttons = {
            '/accounts/logout': 'sign out',
        }
    context['buttons'] = buttons
    return context


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        context = get_base_context(request.user.is_authenticated)
        context['form'] = UserCreationForm()
        return render(request, self.template_name, context)

    def post(self, request):
        context = get_base_context(request.user.is_authenticated)
        form = UserCreationForm(request.POST)
        context['form'] = form

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')

        return render(request, self.template_name, context)


@login_required
def show_stream(request):
    context = get_base_context(request.user.is_authenticated)
    return render(request, 'stream.html', context)


def show_main(request):
    context = get_base_context(request.user.is_authenticated)
    if request.user.is_authenticated:
        context['url'] = '/courses'
    else:
        context['url'] = '/accounts/register/'
    return render(request, 'mainpage.html', context)


@login_required
def show_courses(request):
    context = get_base_context(request.user.is_authenticated)
    return render(request, 'courses.html', context)


@login_required
def show_course(request, course_id):
    if not CurrentCourse.objects.filter(email=request.user.email, course_id=course_id).exists():
        current_course = CurrentCourse(course_id=course_id,
                                       name=Course.objects.get(id=course_id).name,
                                       class_number=Course.objects.get(id=course_id).class_number.number,
                                       email=request.user.email)
        current_course.save()
    context = get_base_context(request.user.is_authenticated)
    context['course'] = Course.objects.get(id=course_id)
    return render(request, 'course.html', context)


@login_required
def show_profile(request):
    context = get_base_context(request.user.is_authenticated)
    context['name'] = request.user.username
    context['email'] = request.user.email
    context['current_courses'] = CurrentCourse.objects.filter(email=request.user.email)
    return render(request, 'profile.html', context)
