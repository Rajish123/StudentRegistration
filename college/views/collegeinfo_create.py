from http.client import HTTPResponse
from college.models import CollegeInformation
from student.models import Student
from batch.models import Batch,Semester,Faculty
from college.forms import CollegeInfoForm
from django.shortcuts import render,redirect
from django.http import Http404

def createCollegeInfo(request,id):
    context = {}
    student = Student.get_student_by_id(id)
    if student:
        batches = Batch.get_all_batch()
        semesters = Semester.get_all_semester()
        faculties = Faculty.get_all_fauclty()


        if request.method == "POST":
            batchId = request.POST.get('batch')
            semesterId = request.POST.get('semester')
            facultyId =request.POST.get('faculty')
            tu_registration = request.POST.get('tu_registration_number'),
            symbol_number = request.POST.get('symbol_number')

            batch = Batch.get_batch_by_id(int(batchId))
            semester = Semester.get_semester_by_id(int(semesterId))
            faculty = Faculty.get_faculty_by_id(int(facultyId))
            collegeinfo = CollegeInformation(
                student = student,
                batch = batch,
                semester = semester,
                faculty = faculty,
                tu_registration_number = tu_registration,
                symbol_number = symbol_number
            )
            collegeinfo.save()
            return redirect('college_info:collegeinfo_list')
        else:
            context = {
                'student':student,
                'batches':batches,
                'semesters':semesters,
                'faculties':faculties
            }
            return render(request, 'college/collegeinfo_create.html',context)
    else:
        raise Http404()
        
        
