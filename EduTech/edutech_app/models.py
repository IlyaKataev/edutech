from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Subject(models.Model):
    name = models.TextField(max_length=50)


class Teacher(models.Model):
    name = models.TextField(max_length=50)
    avatar = models.ImageField
    description = models.TextField(max_length=800)
    subject = models.ManyToManyField(Subject)
    objects = models.Manager()


class ClassNumber(models.Model):
    number = models.TextField(max_length=50)


class Course(models.Model):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=800)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    classNumber = models.ForeignKey(to=ClassNumber, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    objects = models.Manager()
