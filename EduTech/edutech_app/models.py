from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Subject(models.Model):
    Name = models.TextField(max_length=50)


class Teacher(models.Model):
    Name = models.TextField(max_length=50)
    Avatar = models.ImageField
    Description = models.TextField(max_length=800)
    subject = models.ManyToManyField(Subject)
    objects = models.Manager()


class ClassNumber(models.Model):
    Number = models.TextField(max_length=50)


class Course(models.Model):
    Name = models.TextField(max_length=50)
    Description = models.TextField(max_length=800)
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    classNumber = models.ForeignKey(to=ClassNumber, on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.CASCADE)
    objects = models.Manager()
