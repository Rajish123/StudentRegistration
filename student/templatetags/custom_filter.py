
from student.models import Student

from django import template

register = template.Library()




@register.filter(name = 'view_edu')
def view_edu(student):
    student = Student.get_student_by_id(student.id)
    eduInfo = student.collegeinformation_set.all().first()
    return eduInfo.id

@register.filter(name = 'view_familyinfo')
def view_familyinfo(student):
    student = Student.get_student_by_id(student.id)
    familyInfo = student.familyinformation_set.all().first()
    return familyInfo.id

@register.filter(name = 'view_collegeinfo')
def view_collegeinfo(student):
    student = Student.get_student_by_id(student.id)
    collegeInfo = student.collegeinformation_set.all().first()
    return collegeInfo.id

    