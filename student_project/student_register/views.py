from django.shortcuts import render,redirect
from .models import Studentregister
from .forms import StudentForm
# Create your views here.
def student_list(request):
        form=Studentregister.objects.all()
        return render(request,'student_list.html',{'form':form}) 
    
def student_form(request,id=0):
    if request.method=='GET':
        if id==0:
            form=StudentForm()
        else:
            student=Studentregister.objects.get(pk=id)
            form=StudentForm(instance=student)
        return render(request,'student_form.html',{'form':form})
    else:
        if id==0:
            form=StudentForm(request.POST)
        else:
            student=Studentregister.objects.get(pk=id)
            form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')        
def student_delete(request,id):
    student=Studentregister.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')