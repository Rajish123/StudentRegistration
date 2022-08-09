from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import render, redirect

from student.models import Student

from django import template

register = template.Library()


@register.filter(name = 'check_eduinfo')
def check_eduinfo(student):
    student = Student.get_student_by_id(student.id)
    eduInfo = student.educationinformation_set.all().exists()
    if eduInfo:
        return True
    return False

@register.filter(name = 'check_familyinfo')
def check_familyinfo(student):
    student = Student.get_student_by_id(student.id)
    eduInfo = student.familyinformation_set.all().exists()
    if eduInfo:
        return True
    return False

@register.filter(name = 'check_collegeinfo')
def check_collegeinfo(student):
    student = Student.get_student_by_id(student.id)
    eduInfo = student.collegeinformation_set.all().exists()
    if eduInfo:
        return True
    return False

